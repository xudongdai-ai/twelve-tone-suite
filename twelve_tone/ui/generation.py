"""Background composition with queue-only communication to the Tk main thread."""

from queue import Empty, Queue
from threading import Thread

from ..composition.engine import AdvancedTwelveToneComposer


class GenerationTask:
    def __init__(self):
        self._results = Queue()
        self.running = False

    def start(self, inputs, language):
        if self.running:
            raise RuntimeError('已有乐谱正在生成。')
        self.running = True

        def generate():
            try:
                composer = AdvancedTwelveToneComposer()
                composer.lang_system.language = language
                self._results.put((True, composer.run_with_inputs(inputs)))
            except Exception as error:
                self._results.put((False, str(error)))

        try:
            Thread(target=generate, daemon=True).start()
        except Exception:
            self.running = False
            raise

    def poll(self):
        try:
            result = self._results.get_nowait()
        except Empty:
            return None
        self.running = False
        return result
