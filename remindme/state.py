import os
from pydantic import BaseModel

STATE_FILE_NAME = "remindme_progress.json"

class State(BaseModel):
    last_version_seen: int = -1
    topic_to_allocated_index_map: dict[str, int] = {}


def create_state_if_missing() -> None:
    if os.path.exists(_get_state_path()):
        return
    
    _save_state(State())


def allocate_next_index_for_topic(topic: str, max: int) -> int | None:
    create_state_if_missing()
    s = _load_state()
    
    result = s.topic_to_allocated_index_map.get(topic, 0)
    
    if result >= max:
        return None
    
    s.topic_to_allocated_index_map[topic] = result + 1

    _save_state(s)
    return result

def _load_state() -> State:
    create_state_if_missing()
    with open(_get_state_path()) as f:
        return State.model_validate_json(f.read())
    
def _save_state(s: State):
    with open(_get_state_path(), "w") as f:
        f.write(s.model_dump_json())

def _get_state_path() -> str:
    return os.path.join(os.getcwd(), STATE_FILE_NAME)