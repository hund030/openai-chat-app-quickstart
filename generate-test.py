import re

# Read the main.bicep file
with open('infra/main.bicep', 'r') as file:
    main_bicep_content = file.read()

# Find all parameter definitions and allowed values
param_pattern = re.compile(r'param\s+(\w+)\s+(\w+)')
allowed_pattern = re.compile(r'@allowed\(\[\s*([^\]]+)\s*\]\)(?:\s*@\w+\([^\)]*\))*\s*param\s+(\w+)\s+(\w+)')

params = param_pattern.findall(main_bicep_content)
allowed_params = allowed_pattern.findall(main_bicep_content)

# Generate the main.test.bicep content
test_bicep_content = """// This file is for doing static analysis and contains sensible defaults
// for PSRule to minimise false-positives and provide the best results.
// This file is not intended to be used as a runtime configuration file.

targetScope = 'subscription'

module test 'main.bicep' = {
  name: 'test'
  params: {
"""

# Add parameters to the test file content
for param_name, param_type in params:
    # Check if the parameter has allowed values
    allowed_value = None
    for allowed_values, allowed_param_name, allowed_param_type in allowed_params:
        if param_name == allowed_param_name:
            allowed_value = allowed_values.split()[0].strip("'")
            break

    if allowed_value:
        test_bicep_content += f"    {param_name}: '{allowed_value}'\n"
    elif param_type == 'string':
        test_bicep_content += f"    {param_name}: 'test'\n"
    elif param_type == 'int':
        test_bicep_content += f"    {param_name}: 1\n"
    elif param_type == 'bool':
        test_bicep_content += f"    {param_name}: true\n"
    else:
        test_bicep_content += f"    {param_name}: null\n"

# Close the params block and module block
test_bicep_content += """  }
}
"""

# Write the generated content to main.test.bicep
with open('infra/main.test.bicep', 'w') as file:
    file.write(test_bicep_content)

print("main.test.bicep file generated successfully.")