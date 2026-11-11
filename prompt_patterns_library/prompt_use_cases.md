# Prompt Use Cases

## Code Quality

- **Refactoring**
  - **Goal**: Improve readability and performance without changing behavior
  - **Input**: Source function in [LANGUAGE]
  - **Output**: Refactored code + explanation of each change

- **Style Enforcement**
  - **Goal**: Enforce consistent naming and formatting
  - **Input**: Code block + [STYLE_GUIDE] (e.g. PEP 8)
  - **Output**: Rewritten code with consistent style

- **Code Review**
  - **Goal**: Find bugs, smells, and security risks before merging
  - **Input**: Diff or file in [LANGUAGE]
  - **Output**: Prioritized list of issues with suggested fixes

## Debugging

- **Error Explanation**
  - **Goal**: Understand what an error or stack trace means
  - **Input**: Error message, stack trace, relevant code
  - **Output**: Plain-language explanation of the cause + likely fix

- **Root Cause Analysis**
  - **Goal**: Find the underlying reason for a failing behavior
  - **Input**: Expected vs actual behavior, code, steps to reproduce
  - **Output**: Ranked list of probable causes with a way to verify each

- **Performance Bottleneck Diagnosis**
  - **Goal**: Locate slow code paths
  - **Input**: Code or profiler output
  - **Output**: Identified bottlenecks + optimization suggestions

## Documentation

- **Docstring and Comment Generation**
  - **Goal**: Document functions and classes clearly
  - **Input**: Source code in [LANGUAGE] + [DOC_FORMAT] (e.g. Google style)
  - **Output**: Code with complete docstrings

- **README Creation**
  - **Goal**: Produce a clear project overview for new users
  - **Input**: Project description, features, setup steps
  - **Output**: Structured README.md (install, usage, examples, license)

- **API Documentation**
  - **Goal**: Describe endpoints for other developers
  - **Input**: Route handlers or OpenAPI snippet
  - **Output**: Endpoint reference with parameters, responses, and examples

## Testing

- **Unit Test Generation**
  - **Goal**: Cover core logic with automated tests
  - **Input**: Function in [LANGUAGE] + [TEST_FRAMEWORK] (e.g. pytest)
  - **Output**: Unit tests including normal cases and edge cases

- **Edge Case Discovery**
  - **Goal**: Identify inputs likely to break the code
  - **Input**: Function or specification
  - **Output**: List of edge cases with expected behavior

- **Test Data Generation**
  - **Goal**: Create realistic sample data for tests
  - **Input**: Data schema or model definition
  - **Output**: Sample dataset (JSON/CSV) covering valid and invalid values
