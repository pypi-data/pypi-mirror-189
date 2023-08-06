#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from ocrfixr import spellcheck

# Define timing function
def time_func(func, *args): #*args can take 0 or more 
  start_time = time.time()
  func(*args)
  end_time = time.time()
  return(end_time-start_time)

def sc(text):
    return(spellcheck(text).fix())



class TestStringMethods(unittest.TestCase):
    
    def test_finds_misreads(self):
        self.assertEqual(spellcheck("Hello, I'm a maile model.")._LIST_MISREADS(), ['maile'])
        self.assertEqual(spellcheck("'I'm not sure', Adam said. 'I can't see it. The wind-n\ow is half-shut.'")._LIST_MISREADS(), [])
        self.assertEqual(spellcheck("income which represented the capital.1 And the")._LIST_MISREADS(), [])
        self.assertEqual(spellcheck("the nature both of the plan and purpose of his work8.")._LIST_MISREADS(), [])
        self.assertEqual(spellcheck("iron, &c. As I could not detect")._LIST_MISREADS(), [])
        self.assertEqual(spellcheck("571. (16) If lighted by a spiritual sun")._LIST_MISREADS(), [])
        self.assertEqual(spellcheck("been, that it violates certain axioms above stated, (18,) which have been")._LIST_MISREADS(), [])
        self.assertEqual(spellcheck("been, that it violates certain axioms above stated, (ee) which have been")._LIST_MISREADS(), [])
        self.assertEqual(spellcheck('333.   “The Journal du Magnetisme of the 10th of March, 1853, had')._LIST_MISREADS(), [])
        self.assertEqual(spellcheck('Be kept open, soft, and tender.” She talked')._LIST_MISREADS(), [])
        self.assertEqual(spellcheck('of the missionaries to do this.1')._LIST_MISREADS(), [])
        self.assertEqual(spellcheck("51, vii., 44; Coac. iii., 91, 92; II. Morb. xlv., 24-28; III. Morb.")._LIST_MISREADS(), [])
        self.assertEqual(spellcheck("And in another place he maketh mention of the")._LIST_MISREADS(), [])
        self.assertEqual(spellcheck("direct progression from F to B or <i>vice versa</i> (the tritone) was ruled out")._LIST_MISREADS(), [])


    def test_ignore_words(self):
       self.assertEqual(spellcheck("I don't understand your aceent", ignore_words = ['aceent'])._LIST_MISREADS(), [])
       self.assertEqual(spellcheck("I don't understand your aceent")._LIST_MISREADS(), ['aceent'])

    
    def test_returns_orig_text_if_no_errors(self):
        self.assertEqual(spellcheck("this text has no issues").fix(), "this text has no issues")


    def test_finds_easy_errors(self):
        self.assertEqual(spellcheck("cut the sh1t").fix(), "cut the shit")
        self.assertEqual(spellcheck("The birds flevv south").fix(), "The birds flew south")


    def test_keeps_trailing_punctuation(self):
        self.assertEqual(spellcheck("Days there were when small trade came to the stoie. Then the young clerk read.").fix(), "Days there were when small trade came to the store. Then the young clerk read.")


    def test_handles_empty_text(self):
        self.assertEqual(spellcheck("").fix(), "")
        
        
    def test_common_scannos(self):
        self.assertEqual(spellcheck("tle").fix(), "the")
        self.assertEqual(spellcheck("Tlie").fix(), "The")
        self.assertEqual(spellcheck("the context makes no sense to help iito fix this scanno").fix(), "the context makes no sense to help into fix this scanno")


    def test_stealth_scannos(self):
        self.assertEqual(spellcheck("the fox arid the hound ran round and round").fix(), "the fox and the hound ran round and round")
        self.assertEqual(spellcheck("They struggled through the arid desert", changes_by_paragraph = "T").fix(), "NOTE: No changes made to text")
        #self.assertEqual(spellcheck("should he he unsuccessful in our").fix(), 'should he be unsuccessful in our') # note: we dropped he/be, as it is too unreliable & slows things down 4-5x

    def test_retains_paragraphs(self):
        self.assertEqual(spellcheck("The birds flevv down\n south").fix(), "The birds flew down\n south")
        self.assertEqual(spellcheck("The birds flevv down\n\n south").fix(), "The birds flew down\n\n south")   
        self.assertEqual(spellcheck("The birds\n flevv down south").fix(), "The birds\n flevv down south")         # context is paragraph-specific, so OCRfixr doesn't see "birds" as relevant. This is designed behavior.


    def test_return_fixes_flag(self):
        self.assertEqual(spellcheck("The birds flevv down\n south",return_fixes = "T").fix(), ["The birds flew down\n south",{("flevv","flew"):1}])
        self.assertEqual(spellcheck("The birds flevv down\n south and wefe quickly apprehended",return_fixes = "T").fix(), ["The birds flew down\n south and were quickly apprehended",{("flevv","flew"):1, ("wefe","were"):1}])


    def test_changes_by_paragraph_flag(self):
        self.assertEqual(spellcheck("The birds flevv down\n south, bvt wefe quickly apprehended\n by border patrol agents", changes_by_paragraph = "T").fix(), "9 Suggest 'flew' for 'flevv'\n7 Suggest 'but' for 'bvt'\n11 Suggest 'were' for 'wefe'")
        # Case - no misspells in the text
        self.assertEqual(spellcheck("by border patrol agents", changes_by_paragraph = "T").fix(), "NOTE: No changes made to text")
        # Case - misspell in the text, but no replacement
        self.assertEqual(spellcheck("In fact, the effect of circine on the human body\n'", changes_by_paragraph = "T").fix(), "NOTE: No changes made to text")
        # Case - multiple fixes in a single line
        self.assertEqual(spellcheck("I hope yov will f1nd all the rnistakes in this sentence. Otherwise, I wlll be very sad.", changes_by_paragraph = "T").fix(), "6 Suggest 'you' for 'yov'\n15 Suggest 'find' for 'f1nd'\n69 Suggest 'will' for 'wlll'")


    def test_fixes_multiple_errors(self):
        self.assertEqual(spellcheck("I hope yov will f1nd all the rnistakes in this sentence. Otherwise, I wlll be very sad.").fix(), "I hope you will find all the rnistakes in this sentence. Otherwise, I will be very sad.")


    def test_disregards_homophones(self):
        # does not change homophone just --> jist
        self.assertEqual(spellcheck("yuh? You’ll be all right. You’re jist like I was when I begun", changes_by_paragraph = "T").fix(), 'NOTE: No changes made to text')
        # changes o --> e suggestions (an exception to the homophone rule)
        self.assertEqual(spellcheck("It is suggested that these words may bo misapprehended. I use them in the sense", changes_by_paragraph = "T").fix(), "36 Suggest 'be' for 'bo'")
        # does not change suggestions that match manually defined "bad" suggestions 
        self.assertEqual(spellcheck("and over dere you will see the house", changes_by_paragraph = "T").fix(), 'NOTE: No changes made to text')


    def test_fixes_mashed_words(self):
        self.assertEqual(spellcheck("It seemed a long time as we sat there in the darkness waiting for the train; but it was perhaps, in fact, less than half anhour.", changes_by_paragraph = "T").fix(), "120 Suggest 'an hour' for 'anhour'")
        # If theres a comma, keep it when separating words
        self.assertEqual(spellcheck("entrance in another large circuit,which all the churches have;", changes_by_paragraph = "T").fix(), "25 Suggest 'circuit, which' for 'circuit,which'")
        self.assertEqual(spellcheck("counted them,/and there were eighty of a side, in very good", changes_by_paragraph = "T").fix(), "7 Suggest 'them, and' for 'them,/and'")
        # Dont retain other punctuation
        self.assertEqual(spellcheck("Jorge d'Abreu and Lopo da Gama went by.order of the", changes_by_paragraph = "T").fix(), "35 Suggest 'by order' for 'by.order'")
        # Catches 1 of 2
        self.assertEqual(spellcheck("happened in such manner that the rumourof itspread throughout", changes_by_paragraph = "T").fix(), "41 Suggest 'it spread' for 'itspread'")
        # splits words separated by periods/commas, as long as the words are valid
        self.assertEqual(spellcheck("I shall.cultivate the foreign legations,' she", changes_by_paragraph = "T").fix(), "1 Suggest 'shall cultivate' for 'shall.cultivate'")
        self.assertEqual(spellcheck("I shall.blarg the foreign legations,' she", changes_by_paragraph = "T").fix(), 'NOTE: No changes made to text')
        self.assertEqual(spellcheck("here, when it was about two hours of the night, a.little more", changes_by_paragraph = "T").fix(), "47 Suggest 'a little' for 'a.little'")
        self.assertEqual(spellcheck('As to good and evil, beautiful and ugly...and what we ought to do and', changes_by_paragraph = "T").fix(), 'NOTE: No changes made to text')
        # keep second word capitalized if separated by a period. Also keep the period
        self.assertEqual(spellcheck('Here is sentence one.Here is sentence two', changes_by_paragraph = "T").fix(), "16 Suggest 'one. Here' for 'one.Here'")
        self.assertEqual(spellcheck("The Adopted Heir. One volume, paper, $1.50,· or cloth, $2.00.", changes_by_paragraph = "T").fix(),  'NOTE: No changes made to text')

    def test_spellcheck_speed_acceptable(self):
        # GOALS
        # 0 misspells = < 0.01 seconds  [V1.4 = 0.002s]
        # 1 misspell = < 0.10 seconds   [V1.4 = 0.074s]
        # additional misspells "cost" the same amount of time (ie. execution scales linearly with # of misspells)  [V1.4 - this seems to hold true]
        self.assertLessEqual(time_func(sc,"this text has no issues"), 0.01)
        self.assertLessEqual(time_func(sc,"He falls ilL."), 0.2) 
        self.assertLessEqual(time_func(sc,"I hope yov will f1nd all the rnistakes in this sentence. Otherwise, I wlll be very sad."), 1)



if __name__ == '__main__':
    unittest.main()