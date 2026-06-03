"""
STATUS: CANDIDATE — NOT CANON
AUTHORITY: NONE
DEPLOYMENT: NONE
"""
from pathlib import Path

from scripts.lattice_kg_lib import extract_markdown_links, markdown_heading_anchors, read_text, resolve_repo_link

ROOT = Path(__file__).resolve().parents[1]


def test_start_here_docs_exist_and_link_to_targets() -> None:
    docs = [
        ROOT / 'docs/START_HERE_KNOWLEDGE_GRAPH.md',
        ROOT / 'docs/START_HERE_AETHERFORGE.md',
        ROOT / 'docs/START_HERE_GPTDREAM.md',
        ROOT / 'docs/START_HERE_GOVERNANCE.md',
    ]
    for path in docs:
        assert path.exists()
        for link in extract_markdown_links(read_text(path)):
            target = resolve_repo_link(ROOT, path.relative_to(ROOT).as_posix(), link['target'])
            assert target is None or (ROOT / target).exists(), f"broken link {link} in {path}"


def test_readme_table_of_contents_links_work() -> None:
    text = read_text(ROOT / 'README.md')
    anchors = markdown_heading_anchors(text)
    toc_targets = [link['target'][1:] for link in extract_markdown_links(text) if link['target'].startswith('#')]
    assert {'foundation', 'knowledge-graph', 'aetherforge', 'gptdream', 'governance', 'tools', 'projects'} <= set(toc_targets)
    assert set(toc_targets) <= anchors


def test_readme_points_to_key_v1_surfaces() -> None:
    text = read_text(ROOT / 'README.md')
    for required in [
        'archive/knowledge_graph/lattice_kg/v1_0/README.md',
        'docs/START_HERE_KNOWLEDGE_GRAPH.md',
        'docs/AETHERFORGE_QUEST_DASHBOARD.md',
        'archive/knowledge_graph/lattice_kg/v1_0/GPTDREAM_SPEC_IMPL_ALIGNMENT_v1.0.md',
    ]:
        assert required in text
