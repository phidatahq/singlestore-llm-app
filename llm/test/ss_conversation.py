import typer
from rich.prompt import Prompt
from typing import Optional, List

from phi.conversation import Conversation
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.singlestore import SingleStoreVector
from phi.storage.conversation.singlestore import SingleStoreConversationStorage

ss_db_url = "mysql+pymysql://admin:passkey@svc-3nb226d8-ee13-47f0-8ca4-2dc820773442-dml.aws-oregon-2.svc.singlestore.com:3306/dbTest"

knowledge_base = PDFUrlKnowledgeBase(
    urls=[
        "https://www.family-action.org.uk/content/uploads/2019/07/meals-more-recipes.pdf"
    ],
    vector_db=SingleStoreVector(
        collection="recipes",
        db_url=ss_db_url,
    ),
)
knowledge_base.load(recreate=False)

storage = SingleStoreConversationStorage(
    table_name="recipe_conversations",
    db_url=ss_db_url,
)


conversation = Conversation(
    knowledge_base=knowledge_base,
    storage=storage,
    add_references_to_prompt=True,
)

conversation.print_response("Tell me a 2 sentence horror story.")


# def llm_app(new: bool = False, user: str = "user"):
#     conversation_id: Optional[str] = None

#     if not new:
#         existing_conversation_ids: List[str] = storage.get_all_conversation_ids(user)
#         if len(existing_conversation_ids) > 0:
#             conversation_id = existing_conversation_ids[0]

#     conversation = Conversation(
#         user_name=user,
#         conversation_id=conversation_id,
#         knowledge_base=knowledge_base,
#         storage=storage,
#         # add_references_to_prompt=True,
#         function_calls=True,
#         show_function_calls=True,
#     )

#     # conversation.knowledge_base.load(recreate=False)
#     print(f"Conversation ID: {conversation.id}\n")
#     while True:
#         message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
#         if message in ("exit", "bye"):
#             break
#         conversation.print_response(message)


# if __name__ == "__main__":
#     typer.run(llm_app)
