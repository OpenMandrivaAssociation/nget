%define rel	1
%define cvs	20080906
%if %cvs
%define	release		%mkrel 0.%{cvs}.%{rel}
%define distname	%{name}-%{cvs}.tar.lzma
%define dirname		%{name}
%else
%define release		%mkrel %{rel}
%define distname	%{name}-%{version}.tar.gz
%define dirname		%{name}-%{version}
%endif

Summary:	Command line news grabber
Name:		nget
Version:	0.28
Release:	%{release}
License:	GPLv2+
Group:		Networking/News
URL:		http://nget.sf.net
Source0:	http://downloads.sourceforge.net/%{name}/%{distname}
Patch0:		nget-0.27.1-debuginfo.patch
Patch1:		nget-0.28-autoheader.patch
Patch3:		nget-0.28-gcc43.patch
BuildRequires:	uu-static-devel
BuildRequires:	pcre-devel
BuildRequires:	popt
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
nget is a command line news grabber. It automatically pieces together
multipart postings for easy retrieval, even substituting parts from multiple
servers. Handles disconnects gracefully, resuming after the last part
successfully downloaded.

%prep
%setup -q -n %{dirname}
%patch0 -p1
%patch1 -p1 -b .autoheader
%patch3 -p1

%build
%if %cvs
./autogen.sh
%endif
%configure2_5x --with-pcre --with-popt
make
	        
%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc .ngetrc Changelog FAQ README TODO
%{_bindir}/*
%{_mandir}/man1/*
