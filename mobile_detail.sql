--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.16
-- Dumped by pg_dump version 9.5.16

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: dict_detail; Type: TABLE; Schema: public; Owner: erp
--

CREATE TABLE public.dict_detail (
    name character varying(30) NOT NULL,
    department character varying(40) NOT NULL,
    birthdaymonth character varying(40),
    id character varying(20)
);


ALTER TABLE public.dict_detail OWNER TO erp;

--
-- Name: employe_mobile_detail; Type: TABLE; Schema: public; Owner: erp
--

CREATE TABLE public.employe_mobile_detail (
    id integer NOT NULL,
    model text NOT NULL,
    price real,
    first_name character(20) NOT NULL,
    last_name character(20),
    age integer,
    sex character(1),
    alive boolean NOT NULL,
    income double precision
);


ALTER TABLE public.employe_mobile_detail OWNER TO erp;

--
-- Name: mobile_detail; Type: TABLE; Schema: public; Owner: erp
--

CREATE TABLE public.mobile_detail (
    id integer NOT NULL,
    model character varying(20) NOT NULL,
    price integer,
    first_name character varying(20)
);


ALTER TABLE public.mobile_detail OWNER TO erp;

--
-- Data for Name: dict_detail; Type: TABLE DATA; Schema: public; Owner: erp
--

COPY public.dict_detail (name, department, birthdaymonth, id) FROM stdin;
shakirmm	it	october	3
mmmm	dentiist	september	4
shakirmm	it	october	3
mmmm	dentiist	september	4
\.


--
-- Data for Name: employe_mobile_detail; Type: TABLE DATA; Schema: public; Owner: erp
--

COPY public.employe_mobile_detail (id, model, price, first_name, last_name, age, sex, alive, income) FROM stdin;
\.


--
-- Data for Name: mobile_detail; Type: TABLE DATA; Schema: public; Owner: erp
--

COPY public.mobile_detail (id, model, price, first_name) FROM stdin;
1	minote4	12000	shakir
2	minote7	16000	moin
4	apple	55000	aquib
6	minote6	16000	arbaz
5	lenovo	20000	shifa
7	lenovo	7000	tez
8	jio	22000	harsh
9	apple	80000	shahid
3	samsung	66000	alsalan
10	micromax	12000	hemal
\.


--
-- Name: employe_mobile_detail_pkey; Type: CONSTRAINT; Schema: public; Owner: erp
--

ALTER TABLE ONLY public.employe_mobile_detail
    ADD CONSTRAINT employe_mobile_detail_pkey PRIMARY KEY (id);


--
-- Name: mobile_detail_pkey; Type: CONSTRAINT; Schema: public; Owner: erp
--

ALTER TABLE ONLY public.mobile_detail
    ADD CONSTRAINT mobile_detail_pkey PRIMARY KEY (id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

