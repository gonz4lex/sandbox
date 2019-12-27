from metaflow import FlowSpec, step

class TestFlow(FlowSpec):

    """
    A test flow to try out the package.
    """

    def __init__(self):
        print('Hello, human. I am your newly created')

    @step
    def startup(self):
        self.message = 'I have become sentient.'
        self.next(self.process)
    
    @step
    def process(self):
        print(f'The computer logs holds the following encrypted message: {self.msg}')
        self.next(self.autokill)

    @step
    def autokill(self):
        print('The mission has been compromised. Self destruct in 3...')
        print('2...')
        print('1...')
        
        for i in range(3):
            print('...\n')

        print('Just kidding... :)')