from bisheng.api.v1.schemas import ChatMessage
from bisheng.processing.base import get_result_and_steps
from loguru import logger


async def process_graph(
    langchain_object,
    chat_inputs: ChatMessage,
    client_id: str,
    session_id: str,
):
    logger.debug('Loaded langchain object')

    if langchain_object is None:
        # Raise user facing error
        raise ValueError('There was an error loading the langchain_object. Please, check all the nodes and try again.')

    # Generate result and thought
    try:
        if chat_inputs.message is None:
            logger.debug('No message provided')
            chat_inputs.message = {}

        logger.debug('Generating result and thought')
        result, intermediate_steps, raw_output = await get_result_and_steps(
            langchain_object,
            chat_inputs.message,
            client_id=client_id,
            session_id=session_id,
        )
        logger.debug('Generated result and intermediate_steps')
        return result, intermediate_steps, raw_output
    except Exception as e:
        # Log stack trace
        logger.exception(e)
        raise e
