from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI-Driven Customer Support Agent API",
    description="API för SaaS-baserad AI-kundsupportagent för fastighetsbolag",
    version="0.1.0",
)

# Konfigurera CORS för att tillåta anrop från frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ändra detta i produktion
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Välkommen till AI-kundsupportagentens API"}


@app.get("/health")
async def health_check():
    return {"status": "hälsosam"}


# Importera och inkludera routers från api-moduler
# from app.api import company, agent, call, ticket, integration

# app.include_router(company.router)
# app.include_router(agent.router)
# app.include_router(call.router)
# app.include_router(ticket.router)
# app.include_router(integration.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
