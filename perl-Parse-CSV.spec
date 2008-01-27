#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Parse
%define	pnam	CSV
Summary:	Parse::CSV - Highly flexible CVS parser for large files
Name:		perl-Parse-CSV
Version:	1.00
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Parse/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	16089fae987c5d52c0a13acdfc478632
URL:		http://search.cpan.org/dist/Parse-CSV/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Params-Util >= 0.17
BuildRequires:	perl-Text-CSV_XS >= 0.23
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::CSV_XS is the standard parser for CSV files. It is fast as hell,
but unfortunately it can be a bit verbose to use.

A number of other modules have attempted to put usability wrappers around
this venerable module, but they have all focussed on parsing the entire
file into memory at once.

This method is fine unless your CSV files start to get large. Once that
happens, the only existing option is to fall back on the relatively slow
and heavyweight XML::SAXDriver::CSV module.

Parse::CSV fills this functionality gap. It provides a flexible
and light-weight streaming parser for large, extremely large, or
arbitrarily large CSV files.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Parse/*.pm
%{_mandir}/man3/*
