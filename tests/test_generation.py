from threading import Event
import unittest
from unittest.mock import patch

from twelve_tone.ui.generation import GenerationTask


class GenerationTests(unittest.TestCase):
    def test_worker_passes_result_without_tk(self):
        completed = Event()
        task = GenerationTask()
        with patch('twelve_tone.ui.generation.AdvancedTwelveToneComposer') as factory:
            def compose(inputs):
                self.assertEqual(inputs, ('inputs',))
                completed.set()
                return '/tmp/test-score.xml'
            factory.return_value.run_with_inputs.side_effect = compose
            task.start(('inputs',), 'en-US')
            self.assertTrue(completed.wait(5))
            # Join via Queue.get in the test to avoid timing-dependent sleeps.
            result = task._results.get(timeout=5)
            task._results.put(result)
            self.assertEqual(task.poll(), (True, '/tmp/test-score.xml'))
            self.assertFalse(task.running)
            self.assertEqual(factory.return_value.lang_system.language, 'en-US')

    def test_worker_error_can_be_displayed_on_main_thread(self):
        task = GenerationTask()
        with patch('twelve_tone.ui.generation.AdvancedTwelveToneComposer', side_effect=ValueError('bad row')):
            task.start((), 'zh-CN')
            result = task._results.get(timeout=5)
            task._results.put(result)
        self.assertEqual(task.poll(), (False, 'bad row'))
        self.assertFalse(task.running)

    def test_empty_poll_and_duplicate_start(self):
        task = GenerationTask()
        self.assertIsNone(task.poll())
        task.running = True
        with self.assertRaises(RuntimeError):
            task.start((), 'zh-CN')
