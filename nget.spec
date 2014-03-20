%define cvs 20080906

Summary:	Command line news grabber
Name:		nget
Version:	0.28
Release:	0.%{cvs}.2
License:	GPLv2+
Group:		Networking/News
Url:		http://nget.sf.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{cvs}.tar.lzma
Patch0:		nget-0.27.1-debuginfo.patch
# Fix a bug in aclocal.m4 which causes autoheader to fail - AdamW
# 2008/09
Patch1:		nget-0.28-autoheader.patch
# Fix build with GCC 4.3
Patch2:		nget-0.28-gcc43.patch
BuildRequires:	popt
BuildRequires:	uu-static-devel
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(zlib)

%description
nget is a command line news grabber. It automatically pieces together
multipart postings for easy retrieval, even substituting parts from multiple
servers. Handles disconnects gracefully, resuming after the last part
successfully downloaded.

%files
%doc .ngetrc Changelog FAQ README TODO
%{_bindir}/*
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1 -b .autoheader
%patch2 -p1

%build
%if %{cvs}
./autogen.sh
%endif
%configure2_5x --with-pcre --with-popt
make

%install
%makeinstall

