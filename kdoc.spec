Summary:	A perl program to produce html files from javadoc-style comments
Summary(de):	Ein Perl Programm um html Dateien aus javadoc ähnlichen Kommentaren zu erzeugen
Summary(pl):	Narzêdzie do robienia dokumentacji html z komentarzy
Name:		kdoc
Version:	1.17
Release:	1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
Source0:	%{name}-%{version}.tar.gz
#Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdoc-%{version}.tar.bz2
URL:		http://www.ph.unimelb.edu.au/~ssk/kde/kdoc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A perl program to produce html files from javadoc-style comments.

%description -l de
Ein Perl Programm um html Dateien aus javadoc ähnlichen Kommentaren zu
erzeugen.

%description -l pl
Program w perlu do robienia dokumentacji w html na podstawie
komentarzy w stylu javadoc.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf doc/CREDITS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/CREDITS.gz doc/example.h doc/kdoc.html
%{_mandir}/man1/kdoc.1*
%{_mandir}/man1/qt2kdoc.1*
%attr(755,root,root) %{_bindir}/kdoc
%attr(755,root,root) %{_bindir}/qt2kdoc
%dir %{_datadir}/kdoc
%{_datadir}/kdoc/Ast.pm
%{_datadir}/kdoc/kdocHTML.pm
%{_datadir}/kdoc/kdocTeX.pm
%{_datadir}/kdoc/kdocMan.pm
