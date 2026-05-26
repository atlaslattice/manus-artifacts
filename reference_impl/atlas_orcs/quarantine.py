from .state import Artifact


def quarantine(artifact: Artifact) -> Artifact:
    if artifact.state != "quarantined":
        artifact.lineage.append(artifact.state)
        artifact.state = "quarantined"
    return artifact
