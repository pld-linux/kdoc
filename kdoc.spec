Summary:	A perl program to produce html files from javadoc-style comments.
Summary(de):	Ein Perl Programm um html Dateien aus javadoc ähnlichen Kommentaren zu erzeugen.
Name:		kdoc
Version:	1.17
Release:	1
Copyright:	GPL
Group:		Utilities/Text
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A perl program to produce html files from javadoc-style comments.

%description -l de
Ein Perl Programm um html Dateien aus javadoc ähnlichen Kommentaren zu erzeugen.

%prep
%setup -q

%build
./configure --prefix=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
gzip -9 $RPM_BUILD_ROOT/usr/man/man?/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/CREDITS
%doc doc/example.h
%doc doc/kdoc.html
/usr/man/man1/kdoc.1.gz
/usr/man/man1/qt2kdoc.1.gz
/usr/bin/kdoc
/usr/bin/qt2kdoc
/usr/share/kdoc/Ast.pm
/usr/share/kdoc/kdocHTML.pm
/usr/share/kdoc/kdocTeX.pm
/usr/share/kdoc/kdocMan.pm
