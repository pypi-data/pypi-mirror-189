import sys

from lupin_grognard.core.config import (
    SUCCESS,
    FAILED,
    TITLE_FAILED,
    BODY_FAILED,
    MERGE_FAILED,
    COMMIT_TYPE_MUST_HAVE_SCOPE,
)


class ErrorCount:
    def __init__(self):
        self.body_error = 0
        self.feat_scope_error = 0
        self.title_error = 0
        self.merge_error = 0
        self.generic_type_scope_error_message = []

    def increment_body_error(self):
        self.body_error += 1

    def increment_feat_scope_error(self):
        self.feat_scope_error += 1

    def increment_title_error(self):
        self.title_error += 1

    def increment_merge_error(self):
        self.merge_error += 1

    def add_generic_type_scope_error_message(self, message):
        self.generic_type_scope_error_message.append(message)

    def error_report(self):
        if not (self.title_error + self.body_error + self.merge_error):
            print(SUCCESS)
        else:
            print(FAILED)
            print(
                f"Errors found: {self.title_error + self.body_error + self.merge_error}"
            )
            if self.title_error > 0:
                print(TITLE_FAILED)
            if self.body_error > 0:
                print(BODY_FAILED)
            if self.merge_error > 0:
                print(MERGE_FAILED)
            if self.feat_scope_error > 0:
                print(COMMIT_TYPE_MUST_HAVE_SCOPE)
            if self.generic_type_scope_error_message:
                for error_message in self.generic_type_scope_error_message:
                    print(error_message)
            sys.exit(1)
