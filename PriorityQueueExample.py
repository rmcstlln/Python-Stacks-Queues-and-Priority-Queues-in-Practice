from queues import PriorityQueue

@dataclass
class Message:
    event: str


CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")

wipers < hazard_lights

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, wipers)
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, Message("ABS engaged"))
messages.enqueue_with_priority(IMPORTANT, hazard_lights)

messages.dequeue()
print(messages)
