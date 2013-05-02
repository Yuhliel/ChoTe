#coding=UTF-8
import sys
import ply.lex as lex

#Lista con los tokens de las palabras reservadas del compilador.
reserved = {
	'begin'	  	:	'BEGIN'		,
	'main'	  	:	'MAIN'	 	,
	'return'  	:	'RETURN'	,
	'function'	:	'FUNCTION' 	,
	'read'		:	'READ'		,	
	'print'		:	'PRINT'		,	
	'end'	 	:	'END'		,
	'void'		:	'VOID'		,
	'boolean'	:	'BOOLEAN'	,
	'int'		:	'INT'		,
	'double'	:	'DOUBLE'	,
	#'char'		:	'CHAR'		,
	'String'	:	'STRING'	,
	'if'		:	'IF'		,
	'else'		:	'ELSE'		,
	'for'		:	'FOR'		,
	'true'		:	'TRUE'		,
	'false'		:	'FALSE'		,
	'while'		:	'WHILE'		
	}

#Lista con los tokens de los operadores del compilador.
tokens = [
	'ID'								,	
	'OPEN_BRACE'						,	
	'OPEN_PAREN'						,	
	'OPEN_BRACKET'						,	
	'CLOSE_BRACE'						,	
	'CLOSE_PAREN'						,	
	'CLOSE_BRACKET'						,		
	'SEMI_COLON'						,	
	'COMMA'								,	
	'CINT'								,		
	'CDOUBLE'							,	
	'CSTRING'							,
	'ASSIGN'							,	
	'AND'								,	
	'OR'								,	
	'NEGATION'							,
	'GREATER_THAN' 						,	
	'LESS_THAN'							,	
	'DIFFERENT'							,	
	'GREAT_EQUAL'						,	
	'LESS_EQUAL'						,		
	'EQUALS'							,	
	'PLUS'								,	
	'MINUS'								,	
	'TIMES'								,	
	'DIVIDE'			
	] + list(reserved.values())


#####################################################################################

#Expresiones Regulaes para definir los tokens
t_OPEN_BRACE	=	r'\{'
t_OPEN_PAREN	=	r'\('
t_OPEN_BRACKET	= 	r'\['
t_CLOSE_BRACE	=	r'\}'
t_CLOSE_PAREN	=	r'\)'
t_CLOSE_BRACKET	=	r'\]'
t_SEMI_COLON	=	r'\;'
t_COMMA			=	r'\,'
t_CSTRING		=	r'\"[a-zA-Z_][a-zA-Z0-9_]*\"'
t_ASSIGN		=	r'\='
t_AND			=	r'\&\&'
t_OR			=	r'\|\|'
t_NEGATION		=	r'\!'
t_GREATER_THAN	=	r'\>'
t_LESS_THAN		=	r'\<'
t_DIFFERENT		=	r'\!\='
t_GREAT_EQUAL	=	r'\>\='
t_LESS_EQUAL	=	r'\<\='
t_EQUALS		=	r'\=\='
t_PLUS			=	r'\+'
t_MINUS			=	r'\-'
t_TIMES			=	r'\*'
t_DIVIDE		=	r'\/'
t_ignore		= 	" \t"

def t_ID(t):	
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.type = reserved.get(t.value, 'ID')
	return t
	
def t_CINT(t):
	r'\d+'
	try : 
		t.value = int(t.value)
	except ValueError:													
		print("El numero que deseas almacenar es MUY grande. D= ") 
		t.value = 0
	return t
	
def t_CDOUBLE(t):
	r'[0-9]+\.[0-9]'
	try :
		t.value = float(t.value)
	except ValueError:													
		print("El numero que deseas almacenar es MUY grande. D= ") 
		t.value = 0.00
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
	print("Token Invalido >=( '%s'" % t.value[0])
	t.lexer.skip(1)    

lexer = lex.lex()