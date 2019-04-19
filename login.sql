-- Table: public.login

-- DROP TABLE public.login;

CREATE TABLE public.login
(
  id integer NOT NULL DEFAULT nextval('login_id_seq'::regclass),
  name character varying(50),
  lastname character varying(50),
  email character varying(50),
  logindate date
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.login
  OWNER TO postgres;
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


