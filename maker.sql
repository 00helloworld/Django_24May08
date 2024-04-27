CREATE TABLE `gly` (
`glyid` int(11) NOT NULL auto_increment,
`yhm` VARCHAR(40) default NULL COMMENT '�û���',
`mm` VARCHAR(40) default NULL COMMENT '����',
`xm` VARCHAR(40) default NULL COMMENT '����',  PRIMARY KEY  (`glyid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `jiaoshi` (
`jsid` int(11) NOT NULL auto_increment,
`yhm` VARCHAR(40) default NULL COMMENT '�û���',
`mm` VARCHAR(40) default NULL COMMENT '����',
`xm` VARCHAR(40) default NULL COMMENT '����',
`lxdh` VARCHAR(40) default NULL COMMENT '��ϵ�绰',
`zc` VARCHAR(40) default NULL COMMENT 'ְ��',  PRIMARY KEY  (`jsid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `xuesheng` (
`xsid` int(11) NOT NULL auto_increment,
`yhm` VARCHAR(40) default NULL COMMENT '�û���',
`mm` VARCHAR(40) default NULL COMMENT '����',
`xm` VARCHAR(40) default NULL COMMENT '����',
`lxdh` VARCHAR(40) default NULL COMMENT '��ϵ�绰',
`zy` VARCHAR(40) default NULL COMMENT 'רҵ',  PRIMARY KEY  (`xsid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `jsxx` (
`jsxxid` int(11) NOT NULL auto_increment,
`jsmc` VARCHAR(40) default NULL COMMENT '��������',
`wz` VARCHAR(40) default NULL COMMENT 'λ��',
`bz` VARCHAR(40) default NULL COMMENT '��ע',  PRIMARY KEY  (`jsxxid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `xingqi` (
`xqid` int(11) NOT NULL auto_increment,
`xq` VARCHAR(40) default NULL COMMENT '����',  PRIMARY KEY  (`xqid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `sjd` (
`sjdid` int(11) NOT NULL auto_increment,
`sjd` VARCHAR(40) default NULL COMMENT 'ʱ���',  PRIMARY KEY  (`sjdid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `kecheng` (
`kcid` int(11) NOT NULL auto_increment,
`kcmc` VARCHAR(40) default NULL COMMENT '�γ�����',
`rkjs` VARCHAR(40) default NULL COMMENT '�ον�ʦ',
`sm` VARCHAR(40) default NULL COMMENT '˵��',  PRIMARY KEY  (`kcid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `sksj` (
`sksjid` int(11) NOT NULL auto_increment,
`lsh` VARCHAR(40) default NULL COMMENT '��ˮ��',
`xq` VARCHAR(40) default NULL COMMENT '����',
`sjd` VARCHAR(40) default NULL COMMENT 'ʱ���',
`kc` VARCHAR(40) default NULL COMMENT '�γ�',
`js` VARCHAR(40) default NULL COMMENT '����',  PRIMARY KEY  (`sksjid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `qiandao` (
`qdid` int(11) NOT NULL auto_increment,
`sksj` VARCHAR(40) default NULL COMMENT '�Ͽ�ʱ��',
`xs` VARCHAR(40) default NULL COMMENT 'ѧ��',
`zt` VARCHAR(40) default NULL COMMENT '״̬',
`rq` VARCHAR(40) default NULL COMMENT '����',
`qdsj` VARCHAR(40) default NULL COMMENT 'ǩ��ʱ��',
`qtsj` VARCHAR(40) default NULL COMMENT 'ǩ��ʱ��',
`kc` VARCHAR(40) default NULL COMMENT '�γ�',  PRIMARY KEY  (`qdid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `jsjy` (
`jsjyid` int(11) NOT NULL auto_increment,
`sqh` VARCHAR(40) default NULL COMMENT '�����',
`bt` VARCHAR(40) default NULL COMMENT '����',
`nr` VARCHAR(40) default NULL COMMENT '����',
`js` VARCHAR(40) default NULL COMMENT '����',
`sqrq` VARCHAR(40) default NULL COMMENT '��������',
`sjd` VARCHAR(40) default NULL COMMENT 'ʱ���',
`sqsj` VARCHAR(40) default NULL COMMENT '����ʱ��',
`sqzt` VARCHAR(40) default NULL COMMENT '����״̬',
`yh` VARCHAR(40) default NULL COMMENT '�û�',  PRIMARY KEY  (`jsjyid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;

