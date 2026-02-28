from dataclasses import dataclass
from typing import Any, Dict
import logging

logger = logging.getLogger(__name__)

@dataclass
class EngineConfig:
    name: str = "agentic-convergence"
    max_steps: int = 10
    debug: bool = False

class ConvergenceEngine:
    def __init__(self, config: EngineConfig | Dict[str, Any] | None = None):
        if isinstance(config, dict):
            config = EngineConfig(**config)
        self.config: EngineConfig = config or EngineConfig()
        logger.debug("Engine initialized with config: %s", self.config)

    def step(self, state: Dict[str, Any]) -> Dict[str, Any]:
        state["step_count"] = state.get("step_count", 0) + 1
        return state

    def run(self, initial_state: Dict[str, Any] | None = None) -> Dict[str, Any]:
        state = initial_state or {}
        for _ in range(self.config.max_steps):
            state = self.step(state)
        return state
