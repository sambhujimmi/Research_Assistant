import asyncio
import uuid
import os
import sys
from dotenv import load_dotenv

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from core.videogen import Workflow, Text2VideoTask

load_dotenv()
api_key = os.getenv("HEURIST_API_KEY")
if not api_key:
    raise ValueError("HEURIST_API_KEY environment variable is not set")

async def main():
    # Initialize the workflow
    workflow = Workflow(api_key=api_key, workflow_url="https://sequencer-v2.heurist.xyz")

    # Create a task (e.g., Text2Video)
    task = Text2VideoTask(
        consumer_id=str(uuid.uuid4()),
        prompt="A beautiful sunset over the ocean",
        timeout_seconds=600,
        workflow_id="1"
    )

    # Execute and wait for result
    try:
        result = await workflow.execute_workflow(task)
        print(f"Result: {result}")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Error: {str(e)}")

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())