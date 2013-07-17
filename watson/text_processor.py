import nltk
from nltk.tokenize.regexp import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
import re

STOP_WORDS = ['a','able', 'about', 'above', 'abroad', 'according',
'accordingly', 'across', 'actually', 'adj', 'after', 'afterwards',
'again', 'against', 'ago', 'ahead', "ain't", 'all', 'allow', 'allows',
'almost', 'alone', 'along', 'alongside', 'already', 'also', 'although',
'always', 'am', 'amid', 'amidst', 'among', 'amongst', 'an', 'and',
'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway',
'anyways', 'anywhere', 'apart', 'appear', 'appreciate', 'appropriate',
'are', "aren't", 'around', 'as', "a's", 'aside', 'ask', 'asking',
'associated', 'at', 'available', 'away', 'awfully', 'back', 'backward',
'backwards', 'be', 'became', 'because', 'become', 'becomes', 'becoming',
'been', 'before', 'beforehand', 'begin', 'behind', 'being', 'believe',
'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond',
'both', 'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', "can't",
'caption', 'cause', 'causes', 'certain', 'certainly', 'changes',
'clearly', "c'mon", 'co', 'co.', 'com', 'come', 'comes', 'concerning',
'consequently', 'consider', 'considering', 'contain', 'containing',
'contains', 'corresponding', 'could', "couldn't", 'course', "c's",
'currently', 'dare', "daren't", 'definitely', 'described', 'despite',
'did', "didn't", 'different', 'directly', 'do', 'does', "doesn't",
'doing', 'done', "don't", 'down', 'downwards', 'during', 'each', 'edu',
'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending',
'enough', 'entirely', 'especially', 'et', 'etc', 'even', 'ever',
'evermore', 'every', 'everybody', 'everyone', 'everything',
'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far',
'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed',
'following', 'follows', 'for', 'forever', 'former', 'formerly', 'forth',
'forward', 'found', 'four', 'from', 'further', 'furthermore', 'get',
'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going', 'gone',
'got', 'gotten', 'greetings', 'had', "hadn't", 'half', 'happens',
'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd",
"he'll", 'hello', 'help', 'hence', 'her', 'here', 'hereafter', 'hereby',
'herein', "here's", 'hereupon', 'hers', 'herself', "he's", 'hi', 'him',
'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 'however',
'hundred', "i'd", 'ie', 'if', 'ignored', "i'll", "i'm", 'immediate',
'in', 'inasmuch', 'inc', 'inc.', 'indeed', 'indicate', 'indicated',
'indicates', 'inner', 'inside', 'insofar', 'instead', 'into', 'inward',
'is', "isn't", 'it', "it'd", "it'll", 'its', "it's", 'itself', "i've",
'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known', 'knows', 'last',
'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let',
"let's", 'like', 'liked', 'likely', 'likewise', 'little', 'look',
'looking', 'looks', 'low', 'lower', 'ltd', 'made', 'mainly', 'make',
'makes', 'many', 'may', 'maybe', "mayn't", 'me', 'mean', 'meantime',
'meanwhile', 'merely', 'might', "mightn't", 'mine', 'minus', 'miss',
'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'must',
"mustn't", 'my', 'myself', 'name', 'namely', 'nd', 'near', 'nearly',
'necessary', 'need', "needn't", 'needs', 'neither', 'never', 'neverf',
'neverless', 'nevertheless', 'new', 'next', 'nine', 'ninety', 'no',
'nobody', 'non', 'none', 'nonetheless', 'noone', 'no-one', 'nor',
'normally', 'not', 'nothing', 'notwithstanding', 'novel', 'now',
'nowhere', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old',
'on', 'once', 'one', 'ones', "one's", 'only', 'onto', 'opposite', 'or',
'other', 'others', 'otherwise', 'ought', "oughtn't", 'our', 'ours',
'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'particular',
'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus',
'possible', 'presumably', 'probably', 'provided', 'provides', 'que',
'quite', 'qv', 'rather', 'rd', 're', 'really', 'reasonably', 'recent',
'recently', 'regarding', 'regardless', 'regards', 'relatively',
'respectively', 'right', 'round', 'said', 'same', 'saw', 'say',
'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem',
'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sensible',
'sent', 'serious', 'seriously', 'seven', 'several', 'shall', "shan't",
'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'since',
'six', 'so', 'some', 'somebody', 'someday', 'somehow', 'someone',
'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon',
'sorry', 'specified', 'specify', 'specifying', 'still', 'sub', 'such',
'sup', 'sure', 'take', 'taken', 'taking', 'tell', 'tends', 'th', 'than',
'thank', 'thanks', 'thanx', 'that', "that'll", 'thats', "that's",
"that've", 'the', 'their', 'theirs', 'them', 'themselves', 'then',
'thence', 'there', 'thereafter', 'thereby', "there'd", 'therefore',
'therein', "there'll", "there're", 'theres', "there's", 'thereupon',
"there've", 'these', 'they', "they'd", "they'll", "they're", "they've",
'thing', 'things', 'think', 'third', 'thirty', 'this', 'thorough',
'thoroughly', 'those', 'though', 'three', 'through', 'throughout',
'thru', 'thus', 'till', 'to', 'together', 'too', 'took', 'toward',
'towards', 'tried', 'tries', 'truly', 'try', 'trying', "t's", 'twice',
'two', 'un', 'under', 'underneath', 'undoing', 'unfortunately',
'unless', 'unlike', 'unlikely', 'until', 'unto', 'up', 'upon',
'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using', 'usually',
'v', 'value', 'various', 'versus', 'very', 'via', 'viz', 'vs', 'want',
'wants', 'was', "wasn't", 'way', 'we', "we'd", 'welcome', 'well',
"we'll", 'went', 'were', "we're", "weren't", "we've", 'what',
'whatever', "what'll", "what's", "what've", 'when', 'whence',
'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein',
"where's", 'whereupon', 'wherever', 'whether', 'which', 'whichever',
'while', 'whilst', 'whither', 'who', "who'd", 'whoever', 'whole',
"who'll", 'whom', 'whomever', "who's", 'whose', 'why', 'will',
'willing', 'wish', 'with', 'within', 'without', 'wonder', "won't",
'would', "wouldn't", 'yes', 'yet', 'you', "you'd", "you'll", 'your',
"you're", 'yours', 'yourself', 'yourselves', "you've",
'zero','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','gmt','pst','ist','net','com','www','recipient','mon','tue','wed','thu','fri','sat','sun'
,'email','org','apache','gmail','subject','mailto','class','lib','time','error','info','text','html','plain','question','main','sender','date','day','time'
,'attachments','attachment','bin','usr','source','util','failed','auth','root','copy','mail','lot','fine','part','blogspot','e-mail','blog','txt','var','jar','http','java','user','hadoop',
'monday','tuesday','wednesday','thursday','friday','saturday','sunday',
'january','febraury','march','april','may','june','july','august','september','october','november','december']

class TextProcessor():
    NOUN_TAGS = ['NN','NNS','NNP','NNPS','FW']
    VERB_TAGS = ['VB','VBD','VBG','VBN','VBP','VBZ']
    PRONOUN_TAGS = ['PRP','PRP$']
    QUESTION_WORDS = ['what','where','which','why','when','how']
    MODAL_WORDS = ['would','will','is','be','can','shall','should','could','are','were','do','does','did','was','may','might','must','have','am']
    #class Meta:
        #app_label = 'mail_insights'

    def tokenize(self,text):
        tokens = []
        wordnet_lemmatizer = WordNetLemmatizer()
        tokenizer = RegexpTokenizer('(\$?\d+\.\d+)|(([\w]+-)*[\w]+)')
        tokens += tokenizer.tokenize(text)
        tokens = filter(lambda x: x.lower() not in STOP_WORDS and len(x) >1 ,tokens)
        tokens = map(lambda token: wordnet_lemmatizer.lemmatize(token), tokens)
        return tokens

    def removeNonAscii(self,text): return "".join(filter(lambda x: ord(x)<128, text))

    def sentence_tokenize(self,text):
        sentences = re.compile("[\n\.?]").split(text)
        sentences = filter(lambda sentence: not self.is_blank(sentence),sentences )
        sentences = map(lambda sentence: sentence.strip(),sentences)
        return sentences

    def nltk_sentences(self,text):
        return nltk.sent_tokenize(text)

    def pos_tag(self,tokens):
        return nltk.pos_tag(tokens)

    def extract_nouns(self,text):
        tokens = self.no_stop_tokens(text)
        wordnet_lemmatizer = WordNetLemmatizer()
        pos_tagged_sentence = self.pos_tag(tokens)
        nouns = []
        nouns = filter(lambda token: token[1] in self.NOUN_TAGS,pos_tagged_sentence)
        nouns = map(lambda token: token[0],nouns)
        nouns = filter(lambda x: x.lower() not in STOP_WORDS and len(x) > 2 ,nouns)
        nouns = map(lambda token: wordnet_lemmatizer.lemmatize(token), nouns)
        return nouns


    def no_stop_tokens(self,text):
        tokens = []
        tokenizer = RegexpTokenizer('(\$?\d+\.\d+)|(([\w]+-)*[\w]+)')
        tokens += tokenizer.tokenize(text)
        return tokens

    def is_blank(self,text):
        tokens = self.no_stop_tokens(text)
        return len(tokens) == 0

    def extract_mail_domain(self,mail_id):
        domain_name = mail_id.split('@')[-1]
        return domain_name

    def contains_5wh1(self,sentence):
        tokens = map(lambda x:x.lower(),self.no_stop_tokens(sentence))
        number_of_5wh1_words = len(set(tokens) & set(self.QUESTION_WORDS))
        if number_of_5wh1_words > 0:
            return 1
        return 0

    def starts_with_5wh1(self,sentence):
        tokens = map(lambda x:x.lower(),self.no_stop_tokens(sentence))
        if tokens[0] in self.QUESTION_WORDS:
            return 1
        return 0

    def ends_with_5wh1(self,sentence):
        tokens = map(lambda x:x.lower(),self.no_stop_tokens(sentence))
        if tokens[-1] in self.QUESTION_WORDS:
            return 1
        return 0

    #TO-DO change this to use POS tagging or atleast re-vist
    def starts_with_modal(self,sentence):
        tokens = map(lambda x:x.lower(),self.no_stop_tokens(sentence))
        if tokens[0] in self.MODAL_WORDS:
            return 1
        return 0

    def distance_from_beginning_5wh1(self,sentence):
        tokens = map(lambda x:x.lower(),self.no_stop_tokens(sentence))
        index_of_5wh1 = self.index_of_5wh1(tokens)
        if index_of_5wh1 == -1:
            return 0
        weight_of_5wh1 = 1 - (index_of_5wh1 + 1)/float(len(tokens))
        return weight_of_5wh1

    def distance_from_end_5wh1(self,sentence):
        tokens = map(lambda x:x.lower(),self.no_stop_tokens(sentence))
        index_of_5wh1 = self.index_of_5wh1(tokens)
        if index_of_5wh1 == -1:
            return 0
        weight_of_5wh1 = 1 - (len(tokens) - index_of_5wh1 - 1)/float(len(tokens))
        return weight_of_5wh1


    def verb_exists_after_5wh1(self,sentence):
        tokens = map(lambda x:x.lower(),self.no_stop_tokens(sentence))
        index_of_5wh1 = self.index_of_5wh1(tokens)
        if index_of_5wh1 < -1 or index_of_5wh1 == len(tokens)-1:
            return 0
        tagged_tokens = self.pos_tag(tokens)
        if tagged_tokens[index_of_5wh1 + 1][1] in self.VERB_TAGS:
            return 1
        return -1

    def noun_or_pronoun_exists_after_5wh1(self,sentence):
        tokens = map(lambda x:x.lower(),self.no_stop_tokens(sentence))
        index_of_5wh1 = self.index_of_5wh1(tokens)
        if index_of_5wh1 < -1 or index_of_5wh1 == len(tokens)-1:
            return 0
        tagged_tokens = self.pos_tag(tokens)
        if tagged_tokens[index_of_5wh1 + 1][1] in self.NOUN_TAGS + self.PRONOUN_TAGS:
            return 1
        return -1


    def index_of_5wh1(self,tokens):
        for index,token in enumerate(tokens):
            if token in self.QUESTION_WORDS:
                return index
        return -1

    def extract_simple_question_phrase(self,sentence):
        compound_sentence_delimiters = [',',';','then','but','and','or']
        regex_string = "(?i)("+ "|".join(compound_sentence_delimiters) + ")"
        compound_delimiters = re.compile(regex_string)
        simple_sentences = compound_delimiters.split(sentence)
        simple_sentences = filter(lambda sent: sent.lower() not in compound_sentence_delimiters,simple_sentences)

