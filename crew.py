from crewai import Crew
from agents import sales_rep_agent, lead_sales_rep_agent
from tasks import lead_profiling_task, personalized_outreach_task

crew = Crew(
    agents=[sales_rep_agent, lead_sales_rep_agent],
    tasks=[lead_profiling_task, personalized_outreach_task],
    verbose=2,
    memory=True
)
