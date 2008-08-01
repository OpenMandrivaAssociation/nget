Summary:	Command line news grabber
Name:		nget
Version:	0.27.1
Release:	%mkrel 1
License:	GPL
Group:		Networking/News
URL:		http://nget.sf.net
Source0:	http://prdownloads.sourceforge.net/nget/%name-%version.tar.bz2
# (fc) 0.27.1-0.3mdk reduce memory usage (deteman)
Patch0:		nget-0.27.1-memopt.patch
# (fc) 0.27.1-0.3mdk fix optflags (CVS)
Patch1:		nget-0.27.1-optflags.patch
Patch2:		nget-0.27.1-debuginfo.patch
Patch3:		nget-0.27.1-gcc43.patch
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

%setup -q
%patch0 -p1 -b .memopt
%patch1 -p1 -b .optflags
%patch2 -p1
%patch3 -p1

#needed by patch1
autoconf

%build

%configure2_5x --with-pcre --with-popt
%make
	        
%install
rm -rf %{buildroot}

%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc .ngetrc COPYING Changelog FAQ README TODO
%{_bindir}/*
%{_mandir}/man1/*
