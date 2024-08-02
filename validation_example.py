# Import the Great Expectations library
import great_expectations as gx

# Initialize a Great Expectations context
# This context is the main entry point for using Great Expectations
context = gx.get_context()

# Retrieve a pre-configured checkpoint named "example checkpoint"
# Checkpoints are a way to package expectations and data sources for validation
checkpoint = context.get_checkpoint("example checkpoint")

# Run the checkpoint to validate the data
# This will execute all expectations associated with this checkpoint
checkpoint_run_results = checkpoint.run()

# Print the results of the checkpoint run
# This will show whether the data passed or failed the expectations
print(checkpoint_run_results)