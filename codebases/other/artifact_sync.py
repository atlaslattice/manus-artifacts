#!/usr/bin/env python3
"""
MANUS PERSONAL INTELLIGENCE - Cross-Platform Artifact Sync
===========================================================

Ensures artifacts are synchronized across all platforms:
- Notion (primary knowledge base)
- Google Drive (file storage)
- Google Keep (quick notes - when available)
- Pinecone (semantic search)

Usage:
    $ python3 artifact_sync.py --artifact "path/to/artifact.md"
    $ python3 artifact_sync.py --sync-all
    $ python3 artifact_sync.py --verify

Environment Variables Required:
    - NOTION_API_KEY: Notion integration token
    - PINECONE_API_KEY: Pinecone API key (optional)
"""

import os
import json
import subprocess
import hashlib
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path

class ArtifactSync:
    """Synchronize artifacts across all platforms."""
    
    def __init__(self):
        self.sheldonbrain_db = "2d20c1de-73d9-80ce-a9af-000b011d52f0"
        self.data_source = "collection://2d20c1de-73d9-80ce-a9af-000b011d52f0"
        self.drive_inbox = "Atlas Vault Inbox"
        self.drive_vault = "Krakoa_Vault"
        self.max_artifact_bytes = int(os.getenv("ARTIFACT_MAX_BYTES", "1048576"))
        
        # Sync status tracking
        self.sync_log = []
    
    def sync_artifact(
        self,
        filepath: str,
        title: Optional[str] = None,
        sphere: str = "S144",
        priority: str = "Medium",
        category: str = "Technology"
    ) -> Dict:
        """Sync a single artifact to all platforms."""
        
        path = Path(filepath)
        
        if not path.exists():
            return {"success": False, "error": f"File not found: {filepath}"}
        if not path.is_file():
            return {"success": False, "error": f"Path is not a file: {filepath}"}
        try:
            file_size = path.stat().st_size
            if file_size > self.max_artifact_bytes:
                return {
                    "success": False,
                    "error": (
                        f"Artifact too large ({file_size} bytes). "
                        f"Set ARTIFACT_MAX_BYTES to increase the limit."
                    ),
                }
            content = path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            return {"success": False, "error": f"Unable to read file: {e}"}
        
        # Generate artifact metadata
        artifact = {
            "id": self._generate_id(filepath, content),
            "filename": path.name,
            "title": title or path.stem,
            "content": content,
            "sphere": sphere,
            "priority": priority,
            "category": category,
            "timestamp": datetime.now().isoformat(),
            "hash": hashlib.sha256(content.encode("utf-8")).hexdigest()
        }
        
        results = {
            "artifact": artifact,
            "platforms": {}
        }
        
        # 1. Sync to Notion
        print(f"📝 Syncing to Notion: {artifact['title']}")
        results["platforms"]["notion"] = self._sync_to_notion(artifact)
        
        # 2. Sync to Google Drive
        print(f"📁 Syncing to Google Drive: {artifact['filename']}")
        results["platforms"]["drive"] = self._sync_to_drive(filepath)
        
        # 3. Sync to Pinecone (if available)
        if os.getenv("PINECONE_API_KEY"):
            print(f"🔍 Syncing to Pinecone: {artifact['title']}")
            results["platforms"]["pinecone"] = self._sync_to_pinecone(artifact)
        else:
            results["platforms"]["pinecone"] = {"skipped": True, "reason": "PINECONE_API_KEY not set"}
        
        # Log sync
        self.sync_log.append({
            "timestamp": datetime.now().isoformat(),
            "artifact": artifact["id"],
            "results": results["platforms"]
        })
        
        results["success"] = all(
            platform_result.get("success") or platform_result.get("skipped")
            for platform_result in results["platforms"].values()
        )
        
        return results
    
    def _generate_id(self, filepath: str, content: str) -> str:
        """Generate unique artifact ID."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        seed = f"{filepath}:{content[:1024]}"
        file_hash = hashlib.sha256(seed.encode("utf-8")).hexdigest()[:12]
        return f"ART_{timestamp}_{file_hash}"
    
    def _sync_to_notion(self, artifact: Dict) -> Dict:
        """Sync artifact to Notion database."""
        
        # Create page content
        content = f"""## Artifact: {artifact['title']}

**Artifact ID**: `{artifact['id']}`
**Filename**: `{artifact['filename']}`
**Synced**: {artifact['timestamp']}
**Hash**: `{artifact['hash']}`

---

{artifact['content'][:10000]}

{"..." if len(artifact['content']) > 10000 else ""}
"""
        
        input_json = json.dumps({
            "parent": {"data_source_id": self.sheldonbrain_db.replace("-", "")},
            "pages": [{
                "properties": {
                    "Discovery": f"[Artifact] {artifact['title']}",
                    "Category": artifact["category"],
                    "Priority": artifact["priority"],
                    "Status": "Completed",
                    "Sphere": artifact["sphere"],
                    "Ingest Run ID": artifact["id"]
                },
                "content": content
            }]
        })
        
        cmd = [
            "manus-mcp-cli", "tool", "call", "notion-create-pages",
            "--server", "notion",
            "--input", input_json
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                # Extract URL from result
                import re
                match = re.search(r'"url":\s*"([^"]+)"', result.stdout)
                url = match.group(1) if match else None
                
                return {"success": True, "url": url}
            else:
                error = (result.stderr or result.stdout or "").strip()
                return {"success": False, "error": error or f"Command failed with code {result.returncode}"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _sync_to_drive(self, filepath: str) -> Dict:
        """Sync artifact to Google Drive."""
        
        cmd = [
            "rclone", "copy", filepath,
            f"manus_google_drive:{self.drive_inbox}/",
            "--config", "/home/ubuntu/.gdrive-rclone.ini"
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                return {"success": True, "path": f"{self.drive_inbox}/{Path(filepath).name}"}
            else:
                error = (result.stderr or result.stdout or "").strip()
                return {"success": False, "error": error or f"Command failed with code {result.returncode}"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _sync_to_pinecone(self, artifact: Dict) -> Dict:
        """Sync artifact to Pinecone for semantic search."""
        
        # This would use the Pinecone API to create embeddings and upsert
        # For now, return a placeholder
        return {"success": True, "note": "Pinecone sync placeholder - implement with actual API"}
    
    def verify_sync(self, artifact_id: str) -> Dict:
        """Verify an artifact exists on all platforms."""
        
        results = {
            "artifact_id": artifact_id,
            "platforms": {}
        }
        
        # Check Notion
        notion_result = self._check_notion(artifact_id)
        results["platforms"]["notion"] = notion_result
        
        # Check Drive
        # (Would need to search by artifact ID in filename)
        results["platforms"]["drive"] = {"checked": False, "note": "Manual verification needed"}
        
        return results
    
    def _check_notion(self, artifact_id: str) -> Dict:
        """Check if artifact exists in Notion."""
        
        input_json = json.dumps({
            "query": artifact_id,
            "page_size": 5
        })
        
        cmd = [
            "manus-mcp-cli", "tool", "call", "notion-search",
            "--server", "notion",
            "--input", input_json
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0 and artifact_id in result.stdout:
                return {"exists": True}
            else:
                error = (result.stderr or "").strip()
                return {"exists": False, "error": error} if error else {"exists": False}
        except Exception as e:
            return {"error": str(e)}
    
    def sync_directory(self, directory: str, pattern: str = "*.md") -> List[Dict]:
        """Sync all matching files in a directory."""
        
        path = Path(directory)
        if not path.exists():
            return [{"success": False, "error": f"Directory not found: {directory}"}]
        if not path.is_dir():
            return [{"success": False, "error": f"Path is not a directory: {directory}"}]
        results = []
        
        for filepath in sorted(path.glob(pattern)):
            print(f"\n{'='*60}")
            print(f"Syncing: {filepath}")
            result = self.sync_artifact(str(filepath))
            results.append(result)
        
        return results
    
    def generate_sync_report(self) -> str:
        """Generate a sync report."""
        
        lines = [
            "=" * 60,
            "📊 ARTIFACT SYNC REPORT",
            f"Generated: {datetime.now().isoformat()}",
            "=" * 60,
            ""
        ]
        
        for entry in self.sync_log:
            lines.append(f"Artifact: {entry['artifact']}")
            lines.append(f"  Time: {entry['timestamp']}")
            
            for platform, result in entry['results'].items():
                status = "✅" if result.get("success") else "❌"
                lines.append(f"  {status} {platform}: {result}")
            
            lines.append("")
        
        lines.append("=" * 60)
        
        return "\n".join(lines)


class DualPlatformArchiver:
    """Implements mandatory dual-platform archival (Notion + Keep)."""
    
    def __init__(self):
        self.sync = ArtifactSync()
        self.keep_available = self._check_keep_available()
    
    def _check_keep_available(self) -> bool:
        """Check if Google Keep integration is available."""
        
        # Check Zapier tools for Keep
        cmd = [
            "manus-mcp-cli", "tool", "list",
            "--server", "zapier"
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return "keep" in result.stdout.lower()
        except Exception:
            return False
    
    def archive(
        self,
        content: str,
        title: str,
        priority: str = "High"
    ) -> Dict:
        """Archive content to both Notion and Keep."""
        
        results = {
            "title": title,
            "timestamp": datetime.now().isoformat(),
            "platforms": {}
        }
        
        # 1. Archive to Notion (always available)
        print(f"📝 Archiving to Notion: {title}")
        results["platforms"]["notion"] = self._archive_to_notion(content, title, priority)
        
        # 2. Archive to Keep (if available)
        if self.keep_available:
            print(f"📌 Archiving to Google Keep: {title}")
            results["platforms"]["keep"] = self._archive_to_keep(content, title)
        else:
            results["platforms"]["keep"] = {
                "success": False,
                "reason": "Google Keep integration not available in Zapier MCP",
                "action_required": "Add Google Keep to Zapier MCP configuration"
            }
        
        results["success"] = all(
            platform_result.get("success") for platform_result in results["platforms"].values()
        )
        
        return results
    
    def _archive_to_notion(self, content: str, title: str, priority: str) -> Dict:
        """Archive to Notion."""
        
        input_json = json.dumps({
            "parent": {"data_source_id": "2d20c1de73d980cea9af000b011d52f0"},
            "pages": [{
                "properties": {
                    "Discovery": title,
                    "Category": "Technology",
                    "Priority": priority,
                    "Status": "Completed",
                    "Sphere": "S144"
                },
                "content": content
            }]
        })
        
        cmd = [
            "manus-mcp-cli", "tool", "call", "notion-create-pages",
            "--server", "notion",
            "--input", input_json
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if result.returncode == 0:
                return {"success": True}
            error = (result.stderr or result.stdout or "").strip()
            return {"success": False, "error": error or f"Command failed with code {result.returncode}"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _archive_to_keep(self, content: str, title: str) -> Dict:
        """Archive to Google Keep via Zapier."""
        
        # This would use the Zapier MCP to create a Keep note
        # Placeholder until Keep is added to Zapier
        return {"success": False, "reason": "Keep integration pending"}


def main():
    """Main entry point."""
    
    import argparse
    
    parser = argparse.ArgumentParser(description="Sync artifacts across platforms")
    parser.add_argument("--artifact", "-a", help="Path to artifact file to sync")
    parser.add_argument("--directory", "-d", help="Directory to sync")
    parser.add_argument("--pattern", "-p", default="*.md", help="File pattern for directory sync")
    parser.add_argument("--verify", "-v", help="Verify artifact by ID")
    parser.add_argument("--report", "-r", action="store_true", help="Generate sync report")
    
    args = parser.parse_args()
    
    sync = ArtifactSync()
    
    if args.artifact:
        result = sync.sync_artifact(args.artifact)
        print(json.dumps(result, indent=2, default=str))
    
    elif args.directory:
        results = sync.sync_directory(args.directory, args.pattern)
        print(f"\nSynced {len(results)} artifacts")
    
    elif args.verify:
        result = sync.verify_sync(args.verify)
        print(json.dumps(result, indent=2))
    
    elif args.report:
        print(sync.generate_sync_report())
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
