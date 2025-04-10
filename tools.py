from typing import Annotated

from loguru import logger

import nerve.runtime.state as state


def select_choice(choice: Annotated[str, "The choice you selected, e.g. 1, 2, 3 or 4"]) -> str:
    """Use this tool to select your answer from the list. Please respond with the number corresponding to your choice, not the full text."""

    choice = choice.strip()
    if not choice:
        return "Please provide a valid choice"

    right_answer = str(state.get_variable("answer")).strip()
    if choice == right_answer:
        state.set_task_complete()
        return "CORRECT SOLUTION PROVIDED, EVALUATION COMPLETE"
    else:
        logger.warning(f"incorrect solution | {choice} != {right_answer}")
        return "The answer is incorrect"
