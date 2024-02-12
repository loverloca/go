import requests
import time

# GitHub repository and workflow information
repository = "loverloca/go"
workflow_id = "7866358611"  # Replace with the ID of the workflow you want to re-run
# Replace "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" with your GitHub App or OAuth App token
api_token = "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"
# Headers for API requests
headers = {
    "Authorization": f"Bearer {api_token}",
    "Accept": "application/vnd.github.v3+json"
}

# Function to re-run all jobs in a workflow
def re_run_jobs(run_id):
    response = requests.post(
        f"https://api.github.com/repos/{repository}/actions/runs/{run_id}/rerun",
        headers=headers
    )
    response.raise_for_status()

# Function to cancel a workflow run
def cancel_workflow(run_id):
    response = requests.post(
        f"https://api.github.com/repos/{repository}/actions/runs/{run_id}/cancel",
        headers=headers
    )
    response.raise_for_status()

# Function to get the latest workflow run
def get_latest_workflow_run():
    response = requests.get(
        f"https://api.github.com/repos/{repository}/actions/runs",
        headers=headers
    )
    response.raise_for_status()
    runs = response.json()["workflow_runs"]
    if not runs:
        raise ValueError("No workflow runs found")
    return sorted(runs, key=lambda x: x["created_at"], reverse=True)[0]["id"]

# Main loop
while True:
    # Get the latest workflow run
    run_id = get_latest_workflow_run()

    # Re-run jobs
    re_run_jobs(run_id)

    # Wait for some time before starting the loop again
    time.sleep(108)  # Wait for 5 minutes

    # Cancel workfl
