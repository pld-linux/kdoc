%include	/usr/lib/rpm/macros.perl
Summary:	A perl program to produce html files from javadoc-style comments
Summary(de):	Ein Perl Programm um html Dateien aus javadoc �hnlichen Kommentaren zu erzeugen
Summary(es):	K Desktop Environment - Sistema de documentaci�n C++ e IDL
Summary(pl):	Narz�dzie do robienia dokumentacji html z komentarzy
Summary(pt_BR):	Ferramenta de documenta��o do KDE
Name:		kdoc
Version:	2.2.2
Release:	2
Epoch:		1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdoc-%{version}.tar.bz2
URL:		http://www.ph.unimelb.edu.au/~ssk/kde/kdoc/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
A perl program to produce html files from javadoc-style comments.

%description -l de
Ein Perl Programm um html Dateien aus javadoc �hnlichen Kommentaren zu
erzeugen.

%description -l es
KDOC crian una documentaci�n de referencia cruzada en bibliotecas IDL
CORBA e en el lenguage C++. Los docs poden ser mesclados en el source
con mensagens especiales en lo mismo.

%description -l pl
Program w perlu do robienia dokumentacji w html na podstawie
komentarzy w stylu javadoc.

%description -l pt_BR
Ferramentas de documenta��o para o KDE.

%prep
%setup -q

%build
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf doc/DESIGN README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/kdoc
%{_mandir}/man*/*
