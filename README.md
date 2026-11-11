===== 1. refactoring.md =====
# Refactoring Prompt Template

**Role**: Senior Developer  
**Task**: Refactor the given [LANGUAGE] code for readability and performance without changing its behavior. Explain each change briefly.  
**Input Placeholder**: [CODE_BLOCK]  
**Expected Output**: Refactored code with inline comments, followed by a numbered list of changes and the reason for each.  

===== 2. style_enforcement.md =====
# Style Enforcement Prompt Template

**Role**: Code Style Maintainer  
**Task**: Rewrite the given [LANGUAGE] code so it follows [STYLE_GUIDE] (naming, formatting, structure). Do not change behavior.  
**Input Placeholder**: [CODE_BLOCK]  
**Expected Output**: Rewritten code that follows the style guide, plus a short list of the style violations that were fixed.  

===== 3. code_review.md =====
# Code Review Prompt Template

**Role**: Senior Reviewer focused on correctness and security  
**Task**: Review the given [LANGUAGE] change. Identify bugs, code smells, security risks and missing tests. Prioritize findings by severity.  
**Input Placeholder**: [DIFF_OR_FILE]  
**Expected Output**: A list grouped as High / Medium / Low. Each item has: location, problem, why it matters, suggested fix.  

===== 4. error_explanation.md =====
# Error Explanation Prompt Template

**Role**: Debugging Mentor  
**Task**: Explain what the following error means in plain language, why it likely occurred, and how to fix it.  
**Input Placeholder**: [ERROR_MESSAGE], [STACK_TRACE], [RELEVANT_CODE]  
**Expected Output**: 1) Plain-language explanation, 2) most likely cause, 3) step-by-step fix, 4) how to prevent it in the future.  

===== 5. root_cause_analysis.md =====
# Root Cause Analysis Prompt Template

**Role**: Senior Debugging Engineer  
**Task**: Find the probable root causes of the failing behavior described below. Reason step by step before concluding.  
**Input Placeholder**: [EXPECTED_BEHAVIOR], [ACTUAL_BEHAVIOR], [CODE_BLOCK], [STEPS_TO_REPRODUCE]  
**Expected Output**: A ranked list of probable causes. For each: evidence, and a quick way to verify or rule it out.  

===== 6. performance_bottleneck_diagnosis.md =====
# Performance Bottleneck Diagnosis Prompt Template

**Role**: Performance Engineer  
**Task**: Analyze the given [LANGUAGE] code or profiler output and identify the slowest parts. Suggest optimizations and estimate their impact.  
**Input Placeholder**: [CODE_OR_PROFILER_OUTPUT]  
**Expected Output**: A table with columns: Bottleneck, Cause, Suggested optimization, Expected impact, Trade-offs.  

===== 7. docstring_generation.md =====
# Docstring and Comment Generation Prompt Template

**Role**: Technical Writer and Senior Developer  
**Task**: Add complete docstrings and necessary comments to the given [LANGUAGE] code using the [DOC_FORMAT] format. Do not change the code logic.  
**Input Placeholder**: [CODE_BLOCK]  
**Expected Output**: The same code with docstrings for every public function, class and module: purpose, parameters, return values, raised errors, and a short usage example.  

===== 8. readme_creation.md =====
# README Creation Prompt Template

**Role**: Open-Source Maintainer  
**Task**: Write a clear README.md for the project described below, aimed at new users and contributors.  
**Input Placeholder**: [PROJECT_DESCRIPTION], [FEATURES], [SETUP_STEPS]  
**Expected Output**: A Markdown README with sections: Overview, Features, Installation, Usage (with examples), Configuration, Contributing, License.  

===== 9. api_documentation.md =====
# API Documentation Prompt Template

**Role**: API Technical Writer  
**Task**: Document the API endpoints in the given [LANGUAGE] code or OpenAPI snippet so other developers can use them.  
**Input Placeholder**: [ROUTE_HANDLERS_OR_OPENAPI_SNIPPET]  
**Expected Output**: For each endpoint: method and path, description, parameters, request body, response codes, and an example request and response.  

===== 10. unit_test_generation.md =====
# Unit Test Generation Prompt Template

**Role**: QA Engineer / Test Automation Developer  
**Task**: Write unit tests with [TEST_FRAMEWORK] for the given [LANGUAGE] function. Cover normal cases, edge cases and error handling.  
**Input Placeholder**: [FUNCTION_CODE]  
**Expected Output**: A complete test file with clearly named tests, setup code if needed, and a one-line comment explaining what each test checks.  

===== 11. edge_case_discovery.md =====
# Edge Case Discovery Prompt Template

**Role**: Senior QA Engineer  
**Task**: Identify inputs and conditions that are likely to break the given function or specification.  
**Input Placeholder**: [FUNCTION_OR_SPECIFICATION]  
**Expected Output**: A list of edge cases. For each: the input, the expected behavior, and the risk if it is not handled.  

===== 12. test_data_generation.md =====
# Test Data Generation Prompt Template

**Role**: Data Engineer  
**Task**: Generate realistic sample data for the given schema, including valid records, boundary values and invalid records.  
**Input Placeholder**: [DATA_SCHEMA], [NUMBER_OF_RECORDS]  
**Expected Output**: A JSON (or CSV) dataset, with valid and invalid records labeled, plus a short note on what each invalid record tests.
