%include	/usr/lib/rpm/macros.perl
Summary:	A perl program to produce html files from javadoc-style comments
Summary(de):	Ein Perl Programm um html Dateien aus javadoc ähnlichen Kommentaren zu erzeugen
Summary(es):	K Desktop Environment - Sistema de documentación C++ e IDL
Summary(pl):	Narzêdzie do robienia dokumentacji html z komentarzy
Summary(pt_BR):	Ferramenta de documentação do KDE
Name:		kdoc
Version:	2.0a54
Release:	1
Epoch:		2
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.kde.org/pub/kde/stable/latest/src/src/%{name}-%{version}.tar.bz2
# Source0-md5:	700d735518698e6bccf3f26590c487f5
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A perl program to produce html files from javadoc-style comments.

%description -l de
Ein Perl Programm um html Dateien aus javadoc ähnlichen Kommentaren zu
erzeugen.

%description -l es
KDOC crian una documentación de referencia cruzada en bibliotecas IDL
CORBA e en el lenguage C++. Los docs poden ser mesclados en el source
con mensagens especiales en lo mismo.

%description -l pl
Program w perlu do robienia dokumentacji w html na podstawie
komentarzy w stylu javadoc.

%description -l pt_BR
Ferramentas de documentação para o KDE.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/DESIGN README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/kdoc
%{_mandir}/man*/*
