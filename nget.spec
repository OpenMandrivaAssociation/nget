%define name nget
%define version 0.27.1
%define release %mkrel 0.4

Summary: Command line news grabber
Name: %name
Version: %version
Release: %release
Group: Networking/News
BuildRoot: %_tmppath/%{name}-buildroot
Url: http://nget.sf.net
Source0: http://prdownloads.sourceforge.net/nget/%name-%version.tar.bz2
# (fc) 0.27.1-0.3mdk reduce memory usage (deteman)
Patch0: nget-0.27.1-memopt.patch.bz2
# (fc) 0.27.1-0.3mdk fix optflags (CVS)
Patch1: nget-0.27.1-optflags.patch.bz2
License: GPL
BuildRequires:	uu-static-devel


%description
nget is a command line news grabber. It automatically pieces together
multipart postings for easy retrieval, even substituting parts from multiple
servers. Handles disconnects gracefully, resuming after the last part
successfully downloaded.

%prep
%setup -q
%patch0 -p1 -b .memopt
%patch1 -p1 -b .optflags

#needed by patch1
autoconf

%build

%configure2_5x --with-pcre --with-popt
%make
	        
%install

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_mandir}/man1/*
%doc .ngetrc COPYING Changelog FAQ README TODO
%{_bindir}/*

