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
# Fix a bug in aclocal.m4 which causes autoheader to fail - AdamW
# 2008/09
Patch1:		nget-0.28-autoheader.patch
# Fix build with GCC 4.3
Patch2:		nget-0.28-gcc43.patch
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
%patch2 -p1

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


%changelog
* Sun Sep 07 2008 Adam Williamson <awilliamson@mandriva.com> 0.28-0.20080906.1mdv2009.0
+ Revision: 282052
- fix patch numbering, comment patches
- don't package COPYING
- rediff gcc43.patch
- add autoheader.patch (fix an error in aclocal.m4 that causes autoheader to
  fail)
- drop optflags.patch (merged upstream)
- new license policy
- bump to current CVS (probably better than the last release, which is years
  old)

  + Oden Eriksson <oeriksson@mandriva.com>
    - build attempt #2
    - sync with nget-0.27.1-8.fc9.src.rpm

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import nget

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Tue Sep 13 2005 Frederic Crozat <fcrozat@mandriva.com> 0.27.1-0.3mdk 
- Patch0 (deteman): reduce memory usage
- Patch1 (CVS): fix optflags

* Mon May 02 2005 Nicolas CHIPAUX <chipaux@mandrakesoft.com> 0.27.1-0.2mdk
- Fix BuildRequires (add uu-static-devel) (found by François Bandet)

* Tue Jan 04 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.27.1-0.1mdk
- mandrakized orginal specfile
