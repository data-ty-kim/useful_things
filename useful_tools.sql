-- 오라클 단축키
/*
CTRL+U          단어의 모든 문자를 대문자로 변환
CTRL+I          단어의 첫 글자만 대문자, 나머지는 소문자로 변환
CTRL+L          단어의 모든 문자를 소문자로 변환
SHIFT+CTRL+T    커서가 위치한 줄 복사
F9              실행
F4              테이블 정보 보기
*/
;

-- 사용자 함수 검색하기
SELECT * FROM USER_SOURCE WHERE TYPE = 'FUNCTION' AND NAME = 'NAME_OF_FUNCTION'
;
