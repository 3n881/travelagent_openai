from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import  FileWriterTool, SerperDevTool
# from .tools.custom_tool import BookingLinksTool  # Import the new tool
from dotenv import load_dotenv

load_dotenv()

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class TravelaiOpenai():
	"""TravelaiOpenai crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def travel_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['travel_agent'],
			tool=SerperDevTool(
				country="India",
				location="",  # This should be passed when creating the agent or set in config
				n_results=10,
			),
			verbose=True,
		)

	@agent
	def weather_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['weather_agent'],
			tools=[SerperDevTool()],
			verbose=True
		)

	@agent
	def attraction_finder_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['attraction_finder_agent'],
			tools=[SerperDevTool()],
			verbose=True
		)

	@agent
	def safety_advisor_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['safety_advisor_agent'],
			tools=[SerperDevTool()],
			verbose=True
		)
  
	@agent
	def budget_calculator_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['budget_calculator_agent'],
			tools=[SerperDevTool()],
			verbose=True
		)
  
	@agent
	def food_recommendation_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['food_recommendation_agent'],
			tools=[SerperDevTool()],
			verbose=True
		)
  
	@agent
	def booking_services_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['booking_services_agent'],
			tools=[],
			verbose=True
		)

  
  

	# @agent
	# def booking_services_agent(self) -> Agent:
	# 	booking_links = {
	# 		'flights': 'https://trip.tp.st/nu9J4ned',  # Trip.com for flights
	# 		'hotels': 'https://trip.tp.st/nu9J4ned',   # Trip.com for hotels
	# 		'activities': 'https://tiqets.tp.st/8gQeAuD3',  # Tiqets for attractions
	# 		'transfers': [
	# 			'https://kiwitaxi.tp.st/nZ8VaGme',     # Kiwitaxi for transfers
	# 			'https://gettransfer.tp.st/f23S4ViC'   # GetTransfer alternative
	# 		]
	# 	}
		
	# 	booking_tool = BookingLinksTool.create(links=booking_links)
		
	# 	return Agent(
	# 		config=self.agents_config['booking_services_agent'],
	# 		tools=[SerperDevTool(), booking_tool],
	# 		verbose=True
	# 	)
  
  

	@agent
	def file_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['file_writer'],
  		    tools=[FileWriterTool()],
			verbose=True
		) 

	@agent
	def pdf_generator_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['pdf_generator_agent'],
			tools=[FileWriterTool()],
			verbose=True
		)
  
	@task
	def find_travel_locations(self) -> Task:
		return Task(
			config=self.tasks_config['find_travel_locations']
		)

	@task
	def find_hotels(self) -> Task:
		return Task(
			config=self.tasks_config['find_hotels']
		)

	@task
	def calculate_trip_budget(self) -> Task:
		return Task(
			config=self.tasks_config['calculate_trip_budget']
		)

	@task
	def provide_weather_updates(self) -> Task:
		return Task(
			config=self.tasks_config['provide_weather_updates']
		)

	@task
	def find_local_attractions(self) -> Task:
		return Task(
			config=self.tasks_config['find_local_attractions']
		)

	@task
	def provide_safety_advisories(self) -> Task:
		return Task(
			config=self.tasks_config['provide_safety_advisories']
		)
  
	@task
	def recommend_food_options(self) -> Task:
		return Task(
			config=self.tasks_config['recommend_food_options']
		)
  
	@task
	def generate_travel_itinerary(self) -> Task:
		return Task(
			config=self.tasks_config['generate_travel_itinerary']
		)
  
	@task
	def recommend_booking_services(self) -> Task:
		return Task(
			config=self.tasks_config['recommend_booking_services']
		)
  
	@task
	def file_writer_task(self) -> Task:
		return Task(
			config=self.tasks_config['file_writer_task']
		)

	@task
	def generate_pdf_report(self) -> Task:
		return Task(
			config=self.tasks_config['generate_pdf_report']
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the TravelaiOpenai crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
