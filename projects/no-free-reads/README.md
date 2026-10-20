# NO FREE READS · Songcraft × Harness² Pilot

**Status:** PROPOSED album / scoped project seed. This folder adds documents and a machine-readable persona seed. It **does not install a running agent**, alter GPT weights, change the upstream Harness² research engine, invoke Suno, or canonize the album.

## Start
- [AGENTS.md](AGENTS.md) gives the project-level active instructions.
- [Moist subagent](sub_agents/moist-decoysona/AGENT.md) defines a bounded project production manager.
- [Seed/Soul/Core JSON](sub_agents/moist-decoysona/seed-soul-core.json) contains role, sonic controls, authority and experiment protocol.
- [Decoy Swamp Pocket production skill](skills/decoy-swamp-pocket-producer/SKILL.md) gives context-triggered production behavior.
- [Suno Style pack](production/suno-style-pack.md) has four copy-paste Style-field prompts and a suggested Exclude baseline.
- [Validator](tests/test_seed.py) checks structural invariants without API credentials.

## Scope
Album concept: NO FREE READS: An Outlands Field Manual. The twelve-track proposal, including title track, FULL WHERE?, STATIC BETWEEN ROUNDS, and THIRD DOOR THEORY, remains exploratory. Moist is manager/producer, **not** a required sung role or fictional character in songs. Prose/code artifact status never equals a rendered Suno song.

## Portability
The subagent charter and skill are stored in a project-local, Harness²-inspired format. Integration into a live Harness² BenchmarkAdapter, Codex/Claude Code role registration, agent dispatch and actual Suno generation remain future implementation work. Existing core Harness² packages are untouched.

## Human authorial boundary
Protected user expression is never silently transformed; only explicit approval promotes material to canon. Creative phases are SEED, EXPERIMENT, CRAFT, COMPLETION and POST_RELEASE. Metric policy defaults to FIREWALLED. Human listening feedback must distinguish heard audio from untested model hypotheses.

## Lineage / governance sources
- Persona mapping (PER-04): https://app.notion.com/p/3d405d32d1a581ddaa1aed7c8ad2be80
- Creative Sovereignty, Taste & Phase Governance v1.0: https://app.notion.com/p/3e705d32d1a5814ab745f7cc76567ec3
- Agent Registry and Delegation Contracts: https://app.notion.com/p/3e605d32d1a58138b950ea09969af71a
- Harness² upstream: https://github.com/google-research/harness2

## Minimal example prompt
> Moist, manage Track 03. Keep its existing narrative and protected lyrics intact. Make three Suno Style candidates changing only the swamp-bubble response density, and explain how each affects the half-time drop. Don't claim audio evaluation; wait for my listening notes.
