#coding=UTF-8
import sys
import collections

from ChoTeLex import tokens
import ply.yacc as yacc

#Jerarquia de operadores
precedence = (
	('nonassoc', 'GREATER_THAN','LESS_THAN', 'GREAT_EQUAL', 'LESS_EQUAL', 'DIFFERENT'),
	('left', 'AND', 'OR'),
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
	('right','ASSIGN')
)

#Ravenous Demon
#Sintaxis


################# PROGRAM #############################################	

def p_program(p):
	'program 	: BEGIN ID OPEN_BRACE full_module masFullModules MAIN full_block CLOSE_BRACE END'

################# ASSIGN #############################################	
	
def p_asssign(p):
	'asssign 	: ID  asssign1 SEMI_COLON'
	
def p_asssign1(p):
	'''asssign1 : OPEN_BRACKET asssign2 
				| ASSIGN expression'''
				
def p_asssign2(p):
	'''asssign2 : expression CLOSE_BRACKET ASSIGN expression
				| CLOSE_BRACKET ASSIGN OPEN_BRACE adata CLOSE_BRACE'''
				
def p_adata(p):
	'''adata : expression adata
			| COMMA expression adata
			|'''

################# BLOCK #############################################	
def p_block(p):
	'block		: OPEN_BRACE module masModule CLOSE_BRACE'
	
def p_masModule(p):
	'''masModule : module masModule
				|'''

################# CONDITION #############################################	
def p_condition(p):
	'condition	: IF OPEN_PAREN exp_expression CLOSE_PAREN block conditionaux'
	
def p_conditionaux(p):
	''' conditionaux	:	 ELSE block 
						|	'''
################# READ #############################################	
					
def p_readd(p):
	'readd	:	READ OPEN_PAREN	ID	COMMA expression CLOSE_PAREN SEMI_COLON'

def p_printt(p):
	'printt	: PRINT OPEN_PAREN exp_expression CLOSE_PAREN SEMI_COLON'
	
################# MODULE #############################################	
	
def p_module(p):
	'''module	: statement 
				| variable
				| f_call'''
				
################# EXP_EXPRESSION #############################################	
	
def p_exp_expression(p):
	 'exp_expression	:	expression	eee'
	
def p_eee(p):
	'''eee	:	OR ee eee
				| AND ee eee
				|'''
	
def p_ee(p):
	'''ee		: expression 
				|'''
				
################# EXPRESSION #############################################	

def p_expression(p):
	'expression : expression1 exp expression2'
	
def p_expression1(p):
	'''expression1 	: NEGATION 
					|'''
	
def p_expression2(p):
	'''expression2 	: GREATER_THAN expression1 exp
					| LESS_THAN expression1 exp
					| DIFFERENT expression1 exp
					| GREAT_EQUAL expression1 exp
					| LESS_EQUAL expression1 exp
					| EQUALS expression1 exp
					|'''
				
################# FULL BLOCK #############################################	
def p_full_block(p):
	'full_block	: OPEN_BRACE full_module masFullBlock CLOSE_BRACE'
	
def p_masFullBlock(p):
	'''masFullBlock : full_module masFullBlock 
					|'''
					
					
################# FULL MODULE #############################################	
def p_full_module(p):
	'''full_module	: statement 
					| variable 
					| functionn
					| f_call'''

					
def p_masFullModules(p):
	'''masFullModules	:	full_module masFullModules
						|'''


################# STATEMENT #############################################	

def p_statement(p):
	'''statement : printt 
				 | readd 
				 | condition 
				 | asssign 
				 | loop'''

################# TYPE #############################################	
	
def p_type(p):
	'''type : VOID 
			| BOOLEAN 
			| INT 
			| DOUBLE 
			| STRING'''

################# VARIABLE #############################################		
def p_variable(p):
	'variable : type var1 SEMI_COLON'

def p_var1(p):
	'''var1 	: OPEN_BRACKET expression CLOSE_BRACKET var2 
		 		| var2'''
	
def p_var2(p):
	'var2 : ID var3'

def p_var3(p):
	'''var3 : COMMA var2 
			|'''
			
################# FOR #############################################		
def p_forr(p):
	'forr : FOR OPEN_PAREN ID ASSIGN const SEMI_COLON expression SEMI_COLON ID expression CLOSE_PAREN block'

################# LOOP #############################################						
def p_loop(p):
	'''loop : forr 
			| whilee'''
			
################# EXP #############################################		
def p_exp(p):
	'exp : term exp1'
	
def p_exp1(p):
	'''exp1 : PLUS term exp1
			| MINUS term exp1
			|'''
			
################# TERM #############################################	
def p_term(p):
	'term : factor term1'
	
def p_term1(p):
	'''term1 : TIMES factor term1 
			| DIVIDE factor term1
			|'''
################# FACTOR #############################################	

def p_factor(p):
	'''factor 	: OPEN_PAREN expression CLOSE_PAREN
				| varconst'''	
			
################# WHILE #############################################	
	
def p_whilee(p):
	'whilee : WHILE OPEN_PAREN exp_expression CLOSE_PAREN block'	

################# F_MODULE #############################################	
	
def p_f_module(p):
	'''f_module : statement 
				| variable 
				| returnn
				| f_call'''

################# F_BLOCK #############################################	
	
def p_f_block(p):
	'f_block 	: OPEN_BRACE f_module masFModule CLOSE_BRACE'
	
def p_masFModule(p):
	'''masFModule : f_module masFModule
				| '''
				
				
################# FUNCTION ##############################################	
	
def p_functionn(p):
	'functionn : FUNCTION type ID OPEN_PAREN params func1 CLOSE_PAREN f_block'
	
def p_func1(p):
	'''func1 	: COMMA params func1
				|'''
				
################# PARAMS #############################################	
	
def p_params(p):
	'''params		: type para1 ID
					|'''
	
def p_para1(p):
	'''para1	: OPEN_BRACKET CLOSE_BRACKET
				|'''

def p_varconst(p):
	'''varconst : const
				| constID'''
				
def p_constID(p):
	'constID : ID masconstID '				
	
def p_masconstID(p):
	'''masconstID : 	OPEN_BRACKET expression CLOSE_BRACKET
					|'''
################# CONST #############################################	

def p_const(p):
	'''const	: CINT
				| CDOUBLE 
				| constbool 
				| CSTRING'''
				 
def p_constbool(p):
	'''constbool : TRUE 
				|	FALSE'''

################# RETURN #############################################	

def p_returnn(p):
	'returnn 	:	RETURN exp_expression SEMI_COLON'

################# F_CALL #############################################	

def p_f_call(p):
	'f_call : ID OPEN_PAREN adata CLOSE_PAREN SEMI_COLON'
	

######################################################################	
###################   SEMANTICA       ################################
######################################################################	

DirOfProceduresAttributes = collections.namedtupled('DirofProcedures', 'TypeOfReturn DirOfCuadruple Params Variables')
Params = {}
Variables = {}
DirOfProcedures = {}

# Error rule for syntax errors
def p_error(p):
   # print "Syntax error in input!"
	print("Error en %s en línea %s" % (p.value, p.lexer.lineno)) 
	
yacc.yacc()
s = open('test', 'r').read()
yacc.parse(s)