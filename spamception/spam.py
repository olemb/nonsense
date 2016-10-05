"""
Spam, spam, spam.

Spam::

    >>> spam, spam, eggs and spam
    (spam(), spam(), spam()) 
"""

class SpamError(Exception):
    pass


class spam(object):
    """Spam."""
    def __init__(self, *spam, **spam_):
        # Spam, spam, spam.
        self.spam = self.eggs = self

    def __call__(self, *spam, **spam_):
        return self

    def __getitem__(self, spam):
        if spam not in ['eggs', 'spam']:
            raise SpamError('spam != spam')

        return self

    def __str__(self):
        return 'spam, spam, wonderful spam'

    def __repr__(self):
        return 'spam()'

    def __radd__(self, spam):
        return self

    def __gt__(self, other):
        return True

eggs = spam = spam()

__all__ = ['eggs', 'spam']
__author__ = 'Spam Spam'
__email__ = 'spam@spam.spam'
__version__ = '0.0.0'
__url__ = 'spam://spam.spam/'
