import pytest
import os
from pathlib import Path
from remindme import state
from remindme.state import State
from remindme.state import STATE_FILE_NAME

def test_state_model__empty_create():
    # When
    s = State()

    # Then
    s.last_version_seen == -1
    s.topic_to_allocated_index_map == {}

def test_create_state_if_missing__generates_default_state_if_no_file(monkeypatch: pytest.MonkeyPatch, tmp_path: Path):
    # Given
    monkeypatch.chdir(tmp_path)

    # When
    state.create_state_if_missing()

    # Then
    s = assert_state(tmp_path)
    assert s == State()
    


def test_create_state_if_missing__does_nothing_if_file_exists(monkeypatch: pytest.MonkeyPatch, tmp_path: Path):
    # Given
    monkeypatch.chdir(tmp_path)
    existing_state = State(last_version_seen=100, topic_to_allocated_index_map={"test": 1})
    write_state(existing_state, tmp_path)

    # When
    state.create_state_if_missing()

    # Then
    s = assert_state(tmp_path)
    assert s == existing_state

def test_allocate_next_index_for_topic__returns_range_to_max(monkeypatch: pytest.MonkeyPatch, tmp_path: Path):
    # Given
    monkeypatch.chdir(tmp_path)

    # Then
    assert state.allocate_next_index_for_topic("test", 3) == 0
    assert state.allocate_next_index_for_topic("test", 3) == 1
    assert state.allocate_next_index_for_topic("test", 3) == 2
    assert state.allocate_next_index_for_topic("test", 3) is None

def test_allocate_next_index_for_topic__restarts_if_state_purged(monkeypatch: pytest.MonkeyPatch, tmp_path: Path):
    # Given
    monkeypatch.chdir(tmp_path)
    state.allocate_next_index_for_topic("test", 1) == 0
    Path.unlink(tmp_path.joinpath(STATE_FILE_NAME))

    # Then
    assert state.allocate_next_index_for_topic("test", 1) == 0
    assert state.allocate_next_index_for_topic("test", 1) is None

def test_allocate_next_index_for_topic__multiple_topics(monkeypatch: pytest.MonkeyPatch, tmp_path: Path):
    # Given
    monkeypatch.chdir(tmp_path)
    state.allocate_next_index_for_topic("test", 1) == 0
    Path.unlink(tmp_path.joinpath(STATE_FILE_NAME))

    # Then
    assert state.allocate_next_index_for_topic("test1", 1) == 0
    assert state.allocate_next_index_for_topic("test2", 1) == 0
    assert state.allocate_next_index_for_topic("test1", 1) is None
    assert state.allocate_next_index_for_topic("test2", 1) is None

def test_allocate_next_index_for_topic__progressive_max(monkeypatch: pytest.MonkeyPatch, tmp_path: Path):
    # Given
    monkeypatch.chdir(tmp_path)
    state.allocate_next_index_for_topic("test", 1) == 0
    Path.unlink(tmp_path.joinpath(STATE_FILE_NAME))

    # Then
    assert state.allocate_next_index_for_topic("test1", 1) == 0
    assert state.allocate_next_index_for_topic("test1", 3) == 1
    assert state.allocate_next_index_for_topic("test1", 3) == 2
    assert state.allocate_next_index_for_topic("test1", 4) == 3
    assert state.allocate_next_index_for_topic("test1", 4) is None

def test_allocate_next_index_for_topic__max_less_than_current_index(monkeypatch: pytest.MonkeyPatch, tmp_path: Path):
    # Given
    monkeypatch.chdir(tmp_path)
    state.allocate_next_index_for_topic("test", 1) == 0
    Path.unlink(tmp_path.joinpath(STATE_FILE_NAME))

    # Then
    assert state.allocate_next_index_for_topic("test1", 3) == 0
    assert state.allocate_next_index_for_topic("test1", 3) == 1
    assert state.allocate_next_index_for_topic("test1", 1) is None

def assert_state(tmp_path) -> State:
    state_path = tmp_path.joinpath(STATE_FILE_NAME)
    assert os.path.exists(state_path)
    
    with open(os.path.join(tmp_path, state.STATE_FILE_NAME)) as f:
        return State.model_validate_json(f.read())

def write_state(s: State, tmp_path):
    with open(os.path.join(tmp_path, state.STATE_FILE_NAME), 'w') as f:
        f.write(s.model_dump_json())