Name:		sipsak
Version: 	0.9.9
Release:	0.1.pre
License: 	GPL
Group: 		Multimedia
Summary: 	SIP test tool
URL: 		http://sipsak.org/
Source0: 	%{name}-%{version}-pre.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-pre-build
Packager:       Denis Lemire <denis@lemire.name>
Vendor:         generic.business
BuildRequires:  glibc-devel libgcc gcc gcc-c++

%description
sipsak is a small command line tool for developers and administrators of Session Initiation Protocol (SIP) applications. 
It can be used for some simple tests on SIP applications and devices.


%prep
%setup -n %{name}-%{version}-pre

%build
%configure
%__make

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT/*
rm -rf $RPM_BUILD_DIR/5{name}*
rm -rf ../file.list.%{name}


%files
%doc AUTHORS ChangeLog README NEWS TODO
/usr/bin/sipsak
/usr/share/man/man1/sipsak.1*
