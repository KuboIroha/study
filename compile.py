import sys

#s��sample.c�̒��g��ǂݍ���ő��
s = open("sample.c", 'r')

def tokenize(s):
    #�����Ă���������s�̂Ȃ��̃J�b�R��replace�Œu�����ăJ�b�R�����邽��split�ŕ���
    return s.replace("("," ( ").replace(")"," ) ").split()

def parse(tokens):
    #�g�[�N����ŏ��̕������擾���Č��̕����񂩂�폜
    token = tokens.pop(0)
    if token == "(":
        #�J�b�R���̌v�Z�ׂ̈ɐV���ɔz��L��錾
        L = []
        while tokens[0] != ")":
            #tokens���X�g�̒��g��')'����Ȃ�����z��L�ɕ������ǉ�
            L.append(parse(tokens))
        tokens.pop(0)
        return L
    elif token == ")":
        #���̒���')'���������Ƃ�������G���[���b�Z�[�W
        raise SyntaxError(") is deficiency")
    else:
        return token