Summary:	A perl program to produce html files from javadoc-style comments
Summary(de):	Ein Perl Programm um html Dateien aus javadoc ähnlichen Kommentaren zu erzeugen
Summary(pl):	Narzêdzie do robienia dokumentacji html z komentarzy
Name:		kdoc
Version:	2.0a53
Release:	1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
Source0:	http://www.ph.unimelb.edu.au/~ssk/kde/%{name}/%{name}-snapshot.tar.gz
#Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdoc-%{version}.tar.bz2
URL:		http://www.ph.unimelb.edu.au/~ssk/kde/kdoc/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix		/usr/X11R6

%description
A perl program to produce html files from javadoc-style comments.

%description -l de
Ein Perl Programm um html Dateien aus javadoc ähnlichen Kommentaren zu
erzeugen.

%description -l pl
Program w perlu do robienia dokumentacji w html na podstawie
komentarzy w stylu javadoc.

%prep
%setup -q -n %{name}

%build
aclocal
autoconf
%configure \
	--prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf doc/DESIGN README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/kdoc
%{_datadir}/kdoc/*.pm
%{_mandir}/man*/*
