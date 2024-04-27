CREATE TABLE `gly` (
`glyid` int(11) NOT NULL auto_increment,
`yhm` VARCHAR(40) default NULL COMMENT '用户名',
`mm` VARCHAR(40) default NULL COMMENT '密码',
`xm` VARCHAR(40) default NULL COMMENT '姓名',  PRIMARY KEY  (`glyid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `jiaoshi` (
`jsid` int(11) NOT NULL auto_increment,
`yhm` VARCHAR(40) default NULL COMMENT '用户名',
`mm` VARCHAR(40) default NULL COMMENT '密码',
`xm` VARCHAR(40) default NULL COMMENT '姓名',
`lxdh` VARCHAR(40) default NULL COMMENT '联系电话',
`zc` VARCHAR(40) default NULL COMMENT '职称',  PRIMARY KEY  (`jsid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `xuesheng` (
`xsid` int(11) NOT NULL auto_increment,
`yhm` VARCHAR(40) default NULL COMMENT '用户名',
`mm` VARCHAR(40) default NULL COMMENT '密码',
`xm` VARCHAR(40) default NULL COMMENT '姓名',
`lxdh` VARCHAR(40) default NULL COMMENT '联系电话',
`zy` VARCHAR(40) default NULL COMMENT '专业',  PRIMARY KEY  (`xsid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `jsxx` (
`jsxxid` int(11) NOT NULL auto_increment,
`jsmc` VARCHAR(40) default NULL COMMENT '教室名称',
`wz` VARCHAR(40) default NULL COMMENT '位置',
`bz` VARCHAR(40) default NULL COMMENT '备注',  PRIMARY KEY  (`jsxxid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `xingqi` (
`xqid` int(11) NOT NULL auto_increment,
`xq` VARCHAR(40) default NULL COMMENT '星期',  PRIMARY KEY  (`xqid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `sjd` (
`sjdid` int(11) NOT NULL auto_increment,
`sjd` VARCHAR(40) default NULL COMMENT '时间段',  PRIMARY KEY  (`sjdid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `kecheng` (
`kcid` int(11) NOT NULL auto_increment,
`kcmc` VARCHAR(40) default NULL COMMENT '课程名称',
`rkjs` VARCHAR(40) default NULL COMMENT '任课教师',
`sm` VARCHAR(40) default NULL COMMENT '说明',  PRIMARY KEY  (`kcid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `sksj` (
`sksjid` int(11) NOT NULL auto_increment,
`lsh` VARCHAR(40) default NULL COMMENT '流水号',
`xq` VARCHAR(40) default NULL COMMENT '星期',
`sjd` VARCHAR(40) default NULL COMMENT '时间段',
`kc` VARCHAR(40) default NULL COMMENT '课程',
`js` VARCHAR(40) default NULL COMMENT '教室',  PRIMARY KEY  (`sksjid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `qiandao` (
`qdid` int(11) NOT NULL auto_increment,
`sksj` VARCHAR(40) default NULL COMMENT '上课时间',
`xs` VARCHAR(40) default NULL COMMENT '学生',
`zt` VARCHAR(40) default NULL COMMENT '状态',
`rq` VARCHAR(40) default NULL COMMENT '日期',
`qdsj` VARCHAR(40) default NULL COMMENT '签到时间',
`qtsj` VARCHAR(40) default NULL COMMENT '签退时间',
`kc` VARCHAR(40) default NULL COMMENT '课程',  PRIMARY KEY  (`qdid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
CREATE TABLE `jsjy` (
`jsjyid` int(11) NOT NULL auto_increment,
`sqh` VARCHAR(40) default NULL COMMENT '申请号',
`bt` VARCHAR(40) default NULL COMMENT '标题',
`nr` VARCHAR(40) default NULL COMMENT '内容',
`js` VARCHAR(40) default NULL COMMENT '教室',
`sqrq` VARCHAR(40) default NULL COMMENT '申请日期',
`sjd` VARCHAR(40) default NULL COMMENT '时间段',
`sqsj` VARCHAR(40) default NULL COMMENT '申请时间',
`sqzt` VARCHAR(40) default NULL COMMENT '申请状态',
`yh` VARCHAR(40) default NULL COMMENT '用户',  PRIMARY KEY  (`jsjyid`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;

