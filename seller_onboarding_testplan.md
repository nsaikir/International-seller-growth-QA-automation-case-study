# Test Plan: Seller Onboarding

## Objective

To validate the end-to-end seller onboarding workflow across UI, API, and DB layers.

## Scope

- UI: Registration form, error messages, navigation
- API: Seller creation, validation, error handling
- DB: Data persistence, referential integrity

## Test Cases

| ID   | Description                         | Type    | Priority |
|------|-------------------------------------|---------|----------|
| TC01 | Verify seller registration UI loads | UI      | High     |
| TC02 | API returns 201 on valid POST       | API     | High     |
| TC03 | DB contains new seller record       | DB      | High     |
| ...  | ...                                 | ...     | ...      |

## Risks

- API downtime
- Incomplete DB transactions
- UI localization issues

See [../docs/risk_analysis.md](../docs/risk_analysis.md) for full details.
