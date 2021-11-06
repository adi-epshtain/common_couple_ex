import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules
import logging as log


def find_most_common_couple(baskets: list) -> tuple:
    """
   :param baskets: list of customers baskets
   :return: tuple consisted of the two items that were bought together in the same basket the most.
   case failed print to error log and return ("", "")
   """
    antecedents = ""
    consequents = ""

    try:
        te = TransactionEncoder()
        te_ary = te.fit(baskets).transform(baskets)
        df = pd.DataFrame(te_ary, columns=te.columns_)

        frequent_itemsets = fpgrowth(df, use_colnames=True)
        log.debug(frequent_itemsets)
        log.debug("#"*100)
        rules = association_rules(frequent_itemsets, metric="confidence")  # rules of the form X -> Y
        log.debug(rules)

        antecedents = list(rules['antecedents'].iloc[0])[0]
        consequents = list(rules['consequents'].iloc[0])[0]
    except Exception as e:
        log.error(f"find most common couple failed with error: {e}")
    return antecedents, consequents
