Feature: Step Data
    Scenario: Frobulator-English
        Given a sample text loaded into the frobulator:
            """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua.
            """
        When we activate the frobulator
        Then we will find it similar to English
