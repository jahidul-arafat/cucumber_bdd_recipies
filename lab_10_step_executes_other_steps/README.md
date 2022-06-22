# Lab_10 Step executes Other Steps

```bash
# Execute the bahave commands
> behave lab_10_step_executes_other_steps/features/tutorial01_step_within_step.feature --tags=scenario_01
> behave lab_10_step_executes_other_steps/features/tutorial01_step_within_step.feature --tags=scenario_02
> behave lab_10_step_executes_other_steps/features/tutorial01_step_within_step.feature --tags=scenario_02, scenario_01
> behave lab_10_step_executes_other_steps/features/tutorial01_step_within_step.feature 
> behave lab_10_step_executes_other_steps/features/tutorial01_step_within_step.feature --tags=scenario_02 --verbose

# To create a JUNIT report
> behave lab_10_step_executes_other_steps --junit
> behave lab_10_step_executes_other_steps myreport --junit

# To create a JSON report
> behave lab_10_step_executes_other_steps -f json.pretty -o my_reports.json

# To create ALLURE report
> brew install allure       # install allure
> pip install allure-behave #allure-behave integration plugin for Python
> allure                    # verify if allure installed successfully
> cd features
> mkdir my_allure           # to create allure report. Must be created inside the features/ directory
> behave -f allure_behave.formatter:AllureFormatter -o my_allure

# start the allure webserver to view the report
> alliure server my_allure
```