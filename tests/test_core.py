from agentic_convergence.core import ConvergenceEngine, EngineConfig

def test_engine_runs_default_steps():
    cfg = EngineConfig(max_steps=3)
    engine = ConvergenceEngine(cfg)
    result = engine.run({})
    assert result.get("step_count") == 3
