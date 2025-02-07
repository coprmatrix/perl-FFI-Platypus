#
# spec file for package perl-FFI-Platypus (Version 2.08)
#
# Copyright (c) 124 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define cpan_name FFI-Platypus
Name:           perl-FFI-Platypus
Version:        2.08
Release:        0
License:   Artistic-1.0 or GPL-1.0-or-later
Summary:        Write Perl bindings to non-Perl libraries with FFI. No XS required
Url:            https://metacpan.org/release/%{cpan_name}
Source0:         https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  (rpm-build-perl or perl-generators)
BuildRequires:  perl(Alien::FFI) >= 0.20
BuildRequires:  perl(autodie)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(constant) >= 1.32
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.12
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.30
BuildRequires:  perl(FFI::CheckLib) >= 0.05
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(parent)
BuildRequires:  perl(Test2::API) >= 1.302015
BuildRequires:  perl(Test2::V0) >= 0.000121
Requires:       perl(autodie)
Requires:       perl(Capture::Tiny)
Requires:       perl(constant) >= 1.32
Requires:       perl(ExtUtils::MakeMaker) >= 7.12
Requires:       perl(FFI::CheckLib) >= 0.05
Requires:       perl(IPC::Cmd)
Requires:       perl(JSON::PP)
Requires:       perl(List::Util) >= 1.45
Requires:       perl(parent)
%{perl_requires}

%description
Platypus is a library for creating interfaces to machine code libraries
written in languages like C, C++, Go, Fortran, Rust, Pascal. Essentially
anything that gets compiled into machine code. This implementation uses at
https://sourceware.org/libffi/ to accomplish this task. at
https://sourceware.org/libffi/ is battle tested by a number of other
scripting and virtual machine languages, such as Python and Ruby to serve a
similar role. There are a number of reasons why you might want to write an
extension with Platypus instead of XS:

* FFI / Platypus does not require messing with the guts of Perl

XS is less of an API and more of the guts of perl splayed out to do
whatever you want. That may at times be very powerful, but it can also be a
frustrating exercise in hair pulling.

* FFI / Platypus is portable

Lots of languages have FFI interfaces, and it is subjectively easier to
port an extension written in FFI in Perl or another language to FFI in
another language or Perl. One goal of the Platypus Project is to reduce
common interface specifications to a common format like JSON that could be
shared between different languages.

* FFI / Platypus could be a bridge to Raku

One of those "other" languages could be Raku and Raku already has an FFI
interface I am told.

* FFI / Platypus can be reimplemented

In a bright future with multiple implementations of Perl 5, each
interpreter will have its own implementation of Platypus, allowing
extensions to be written once and used on multiple platforms, in much the
same way that Ruby-FFI extensions can be use in Ruby, JRuby and Rubinius.

* FFI / Platypus is pure perl (sorta)

One Platypus script or module works on any platform where the libraries it
uses are available. That means you can deploy your Platypus script in a
shared filesystem where they may be run on different platforms. It also
means that Platypus modules do not need to be installed in the platform
specific Perl library path.

* FFI / Platypus is not C or C++ centric

XS is implemented primarily as a bunch of C macros, which requires at least
some understanding of C, the C pre-processor, and some C++ caveats (since
on some platforms Perl is compiled and linked with a C++ compiler).
Platypus on the other hand could be used to call other compiled languages,
like Fortran, Go, Rust, Pascal, C++, or even assembly, allowing you to
focus on your strengths.

* FFI / Platypus does not require a parser

Inline isolates the extension developer from XS to some extent, but it also
requires a parser. The various Inline language bindings are a great
technical achievement, but I think writing a parser for every language that
you want to interface with is a bit of an anti-pattern.

This document consists of an API reference, a set of examples, some support
and development (for contributors) information. If you are new to Platypus
or FFI, you may want to skip down to the EXAMPLES to get a taste of what
you can do with Platypus.

Platypus has extensive documentation of types at FFI::Platypus::Type and
its custom types API at FFI::Platypus::API.

You are *strongly* encouraged to use API level 2 for all new code. There
are a number of improvements and design fixes that you get for free. You
should even consider updating existing modules to use API level 2 where
feasible. How do I do that you might ask? Simply pass in the API level to
the platypus constructor.

 my $ffi = FFI::Platypus->new( api => 2 );

The Platypus documentation has already been updated to assume API level 1.

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes Changes.FFI-Build Changes.FFI-Platypus-Type-StringArray CONTRIBUTING examples README SUPPORT
%license LICENSE

%changelog
