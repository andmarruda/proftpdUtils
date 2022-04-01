CREATE SCHEMA proftpd;

CREATE TABLE proftpd.xferlog(
	id_xferlog BIGSERIAL NOT NULL CONSTRAINT xferlog_pkey PRIMARY KEY,
	datetime TIMESTAMPTZ NOT NULL,
	transfer_time INT NOT NULL,
	remote_host CHARACTER VARYING(50) NOT NULL,
	filesize BIGINT NOT NULL,
	filename TEXT NOT NULL,
	transfer_type CHARACTER VARYING(1) NOT NULL,
	special_action_flag CHARACTER VARYING(1) NOT NULL,
	direction CHARACTER VARYING(1) NOT NULL,
	access_mode CHARACTER VARYING(1) NOT NULL,
	username CHARACTER VARYING(100) NOT NULL,
	service_name CHARACTER VARYING(15) NOT NULL,
	authentication_method CHARACTER VARYING(1) NOT NULL,
	authenticated_user_id CHARACTER VARYING(20) NOT NULL,
	completion_status CHARACTER VARYING(1) NOT NULL,
	CONSTRAINT xferlog_ukey UNIQUE(datetime, remote_host, filename, username)
) with(
oids=false
);
GRANT ALL ON ALL SEQUENCES IN SCHEMA proftpd TO public;
