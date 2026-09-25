COMMIT_MESSAGE: Add public random letter endpoint

# AI Change Log

## Summary
Added a stateless, public `GET /generate-letter` endpoint to the existing FastAPI application.

## Changes made
- Added `generate_random_letter()` using Python's standard-library `random.choice` over uppercase English letters.
- Added the `GeneratedLetter` response schema and the new endpoint while retaining the existing `POST /generate` route unchanged.
- Added `tests/test_main.py`, which verifies the public endpoint returns HTTP 200 and exactly one `letter` key containing a single uppercase `A`–`Z` character.
- Added `start_0c41c493-6451-491b-9fd6-d44388cda958.sh` for deployment-style Uvicorn boot verification.

## Verification
- Syntax/import check passed for the changed Python modules and FastAPI route registration.
- `python -m pytest` (using the available host Python path) passed: 4 tests passed.
- Deployment-script boot verification returned HTTP 200 from `GET /generate-letter` with a valid JSON letter response.

## Scope
No database, persistence, messaging, authentication, external service, or unrelated application behavior was added or changed.
