# Risk Analysis

## Identified Risks

- API endpoint downtime may block onboarding flow.
- DB schema changes may break data validation.
- UI may be inconsistent across browsers.
- AWS resource limits may affect test environment setup.

## Mitigation Strategies

- Monitor endpoints with AWS CloudWatch
- Use versioned DB migrations
- Cross-browser UI tests in CI
- Automated environment setup with CloudFormation
