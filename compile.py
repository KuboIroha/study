import sys

#sにsample.cの中身を読み込んで代入
s = open("sample.c", 'r')

def tokenize(s):
    #入ってきた文字列sのなかのカッコをreplaceで置換してカッコがあるたびsplitで分割
    return s.replace("("," ( ").replace(")"," ) ").split()

def parse(tokens):
    #トークン列最初の文字を取得して元の文字列から削除
    token = tokens.pop(0)
    if token == "(":
        #カッコ内の計算の為に新たに配列Lを宣言
        L = []
        while tokens[0] != ")":
            #tokensリストの中身が')'じゃない限り配列Lに文字列を追加
            L.append(parse(tokens))
        tokens.pop(0)
        return L
    elif token == ")":
        #式の中に')'が無いことを告げるエラーメッセージ
        raise SyntaxError(") is deficiency")
    else:
        return token